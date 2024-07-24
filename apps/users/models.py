from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from apps.users.choices import TypeOfAccount


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    type_of_account = models.CharField(max_length=20, choices=TypeOfAccount.choices())

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['name', 'type_of_account']

    def __str__(self):
        return self.email
