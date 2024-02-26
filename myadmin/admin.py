from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register models with basic customizations

class VenueCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(VenueCategory, VenueCategoryAdmin)

class VenueFacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(VenueFacility, VenueFacilityAdmin)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'address', 'image_display', 'price', 'get_facilities')
    list_filter = ('category',)
    search_fields = ('name', 'address')

    @admin.display(description="image")
    def image_display(self, obj):
        return format_html('<img src="{}" width="50px" height="50px"/>'.format(obj.pf_image.url))
    
    @admin.display(description="Facilities")
    def get_facilities(self, obj):
        return ", ".join([facilities.name for facilities in obj.facilities.all()])

admin.site.register(Venue, VenueAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'venue', 'booking_date', 'booking_time', 'token_money', 'confirmed')
    list_filter = ('confirmed', 'booking_date')
    search_fields = ('user__username', 'venue__name')

admin.site.register(Booking, BookingAdmin)

class VenueManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_venue_names')  # Use the custom method

    def get_venue_names(self, obj):
        return ', '.join(venue.name for venue in obj.venues.all())  # Display venue names

admin.site.register(VenueManager, VenueManagerAdmin)

@admin.register(VenueImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['venue', 'image_display']

    @admin.display(description="image")
    def image_display(self, obj):
        return format_html('<img src="{}" width="50px" height="50px"/>'.format(obj.gallery.url))