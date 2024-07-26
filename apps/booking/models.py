from django.db import models

from apps.property.models import Property
from apps.users.models import User


class Booking(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    apartment = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='booking')
    date_from = models.DateField()
    date_to = models.DateField()
    is_approved_by_landlord = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)