from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'pk': self.pk})