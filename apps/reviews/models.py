from django.db import models

from apps.booking.models import Booking
from apps.users.models import User


class Review(models.Model):
    renter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    rating = models.IntegerField()
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='review')
