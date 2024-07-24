from django.db import models

from apps.users.models import User
from apps.property.type_of_property import PropertyType


class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    property_type = models.CharField(max_length=20, choices=PropertyType.choices())
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
