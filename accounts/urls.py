from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('sign-up/', views.register, name='register'),
    path('profile/', views.profile, name='profile')
]