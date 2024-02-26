from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import Customuser
from myadmin.models import Booking

from .forms import CustomuserCreationForm, CustomuserLoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = CustomuserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')
                else: return redirect(request.session.get('redirect_to'))
            else:
                return render(request, 'accounts/login.html', {'form': form, 'invalid_login': True})
    else:
        form = CustomuserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomuserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now login with your credentials.')
            return redirect('register')
    else:
        form = CustomuserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    if not request.user.is_authenticated: return render(request, 'accounts/login.html')
    context = {
        'bookings': Booking.objects.filter(user__id = request.user.id)
    }
    if request.method == 'POST':
        user = Customuser.objects.get(id = request.user.id)
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.contactnumber = request.POST.get('contact')
        user.save()
    return render(request, 'accounts/profile.html', context)