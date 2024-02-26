import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as user_logout
from django.http import JsonResponse
from myadmin.models import *
from accounts.models import Orders
from datetime import datetime, time
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from home.contants import PaymentStatus

# Create your views here.
razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def index(request):
    request.session['redirect_to'] = request.build_absolute_uri()
    return render(request, 'home/index.html')

def logout(request):
    user_logout(request)
    request.session['redirect_to'] = request.build_absolute_uri()
    return redirect('/')

def venuelist(request, venue_cat):
    venues = Venue.objects.filter(category__name=venue_cat)
    context = {
        'venues': venues
    }
    request.session['redirect_to'] = request.build_absolute_uri()
    return render(request, 'home/venue_list.html', context)

def details(request, venue_cat, venue_id):
    venue = get_object_or_404(Venue, category__name=venue_cat, id=venue_id)
    gallery = VenueImage.objects.filter(venue__id = venue_id)
    context = {
        'venue': venue,
        'gallery': gallery,
        'facilities': venue.facilities.all()
    }
    request.session['redirect_to'] = request.build_absolute_uri()
    return render(request, 'home/details.html', context)

def getR_Order(t_d_D, f_d_D, venue, currency, payment_capture):
    # print(venue)
    amount = venue.price * ((t_d_D - f_d_D).days + 1)
    notes = {
        'booked_date_from': f_d_D.strftime("%Y-%m-%d"),
        'booked_date_to': t_d_D.strftime("%Y-%m-%d")
    }
    return razorpay_client.order.create(dict(amount=amount ,currency=currency, payment_capture=payment_capture, notes=notes))

def getContext(R_order):
    return {
        'razorpay_merchant_key': settings.RAZOR_KEY_ID,
        'callback_url': 'http://127.0.0.1:8000/paymenthandler/',
        'order': R_order
    }

def getOrder(user, R_order, venue):
    order_id = R_order['id']
    user_id = user.id
    order_money = R_order['amount']
    order_INR = R_order['currency']
    return Orders.objects.create(venue = venue, order_id = order_id, user_id = user_id, order_money = order_money, order_INR =order_INR)

def availablity(request, from_date, to_date, venue_cat, venue_name):
    available = True
    bookings = Booking.objects.filter(venue__name=venue_name, venue__category__name=venue_cat)
    f_d_D = datetime.strptime(from_date, '%Y-%m-%d')
    t_d_D = datetime.strptime(to_date, '%Y-%m-%d')
    request.session['booked_date_from'] = f_d_D.strftime("%Y-%m-%d")
    request.session['booked_date_to'] = t_d_D.strftime("%Y-%m-%d")
    venue = Venue.objects.get(category__name=venue_cat, name=venue_name)
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({'redirect': 'http://127.0.0.1:8000/account/login/'})
    if not bookings:
        R_order = getR_Order(t_d_D, f_d_D, venue, 'INR', '1')
        context = getContext(R_order)
        order = getOrder(user, R_order, venue)
        order.save()
        return JsonResponse({'available': available, 'context' : context})
    for booking in bookings:
        if datetime.combine(booking.booked_date_from, time.min) > f_d_D and datetime.combine(booking.booked_date_from, time.min) > t_d_D or datetime.combine(booking.booked_date_to, time.min) < f_d_D: continue
        else: return JsonResponse({'available': not available})
    R_order = getR_Order(t_d_D, f_d_D, venue, 'INR', '1')
    context = getContext(R_order)
    order = getOrder(user, R_order, venue)
    order.save()
    return JsonResponse({'available': available, 'context' : context})

@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            order = Orders.objects.get(order_id = razorpay_order_id)
            order.payment_id = payment_id
            order.signature_id = signature
            order.save()
            if result is not None:
                user = request.user
                venue = order.venue
                booked_date_from = request.session.get('booked_date_from')
                booked_date_to = request.session.get('booked_date_to')
                token_money = order.order_money
                booking = Booking.objects.create(user=user, venue=venue, booked_date_from=booked_date_from, booked_date_to=booked_date_to, token_money=token_money)
                booking.confirmed = True
                booking.save()
                order.booking_id = booking.id
                order.status = PaymentStatus.SUCCESS
                order.save()
                return render(request, 'home/index.html')
            else:
                order.status = PaymentStatus.FAILURE
                order.save()
                return HttpResponseBadRequest('failed')
        except:
            order.status = PaymentStatus.FAILURE
            order.save()
            return HttpResponseBadRequest('failed1')
    else:
        order.status = PaymentStatus.FAILURE
        order.save()
        return HttpResponseBadRequest('failed2')

