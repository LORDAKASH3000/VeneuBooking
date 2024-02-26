from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customuser
# Register your models here.

@admin.register(Customuser)
class CustomuserAdmin(UserAdmin):
    model = Customuser 
    list_display = ('username', 'is_superuser', 'is_active', 'is_staff')
    fieldsets = UserAdmin.fieldsets + ((("Contact info"), {"fields": ('contactnumber',)}),)