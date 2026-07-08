from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = None

    phone = models.CharField(
        max_length=11,
        unique=True
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.phone