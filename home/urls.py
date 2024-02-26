from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('venue_list/<str:venue_cat>/', views.venuelist, name='venue_list'),
    path('logout/', views.logout, name='logout'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('more_details/<str:venue_cat>/<str:venue_id>/', views.details, name='details'),
    path('check_availablity/<str:from_date>/<str:to_date>/<str:venue_cat>/<str:venue_name>/', views.availablity, name='availablity')
]
