# account/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, Permission
from django.db import models
from datetime import datetime
from django.db.models.fields import *
from home.contants import PaymentStatus
from django.utils.translation import gettext_lazy as _

from myadmin.models import Venue

class CustomuserManager(BaseUserManager):
    def create_user(self, username, email, contactnumber, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, contactnumber=contactnumber)
        user.set_password(password)
        user.save(using=self._db)
        user.user_permissions.set(Permission.objects.all())
        return user

    def create_superuser(self, username, email, contactnumber, password=None):
        user = self.create_user(username, email, contactnumber, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Customuser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    contactnumber = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomuserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'contactnumber']

    def __str__(self):
        return self.username
    
    def get_user_permissions(self, obj=None):
        return set()

    def get_all_permissions(self, obj=None):
        return set()

class Orders(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)
    order_id = models.CharField(max_length=30, unique=True)
    user_id = models.CharField(max_length=30, null=True)
    booking_id = models.CharField(max_length=30, null=True)
    order_money = models.FloatField(_("Amount"), null=True, blank=False)
    order_INR = models.CharField(max_length=10, null=True)
    order_date = datetime.now().date()
    order_time = datetime.now().time()
    status = CharField(_("Payment Status"),default=PaymentStatus.PENDING,max_length=254,blank=False,null=False)
    payment_id = models.CharField(_("Payment ID"), max_length=36, null=True, blank=False)
    signature_id = models.CharField(_("Signature ID"), max_length=128, null=True, blank=False)