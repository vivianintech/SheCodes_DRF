from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, default="")
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=300, default="")
    profile_image = models.URLField(default="https://assets.website-files.com/5bff8886c3964a992e90d465/5c00fa3ad82b40e853c9952f_hero-3.svg")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username