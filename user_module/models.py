from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .Managers import CustomUserManager


class CustomUsers(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("COMPANY", 'Company'),
        ("TALENT", 'Talent'),
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    email = models.EmailField(unique=True, max_length=100)
    full_name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    modified_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
