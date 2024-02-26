from django.db import models
from django.conf import settings
from django.utils import timezone

class VenueCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class VenueFacility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Venue(models.Model):
    category = models.ForeignKey(VenueCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    facilities = models.ManyToManyField(VenueFacility, blank=True)
    pf_image = models.ImageField(upload_to='venue_img', blank=True, null=True)

    def __str__(self):
        return self.name

class VenueImage(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)
    gallery = models.ImageField(upload_to='venue_img', blank=True, null=True)

    def __str__(self):
        return self.venue.name

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    booking_date = models.DateField(default=timezone.now)
    booking_time = models.TimeField(default=timezone.now)
    booked_date_from = models.DateField(null=True)
    booked_date_to = models.DateField(null=True)
    token_money = models.FloatField(null=True, blank=False)
    confirmed = models.BooleanField(default=False)
    def __str__(self):
        return self.venue.name

class VenueManager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    venues = models.ManyToManyField(Venue, related_name='managers')
    def __str__(self):
        return self.user.username
