from django.contrib import admin
from accounts.models import Orders

# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user_id', 'booking_id', 'order_money', 'order_INR', 'status')