from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    AUT = "Author"
    SUB = "Subscriber"
    ROLES = (
        (AUT, 'Author'),
        (SUB, 'Subscriber'),
    )

    email = models.EmailField(
        _('email address'),
        unique=True
    )
    role = models.CharField(max_length=30, choices=ROLES, default=SUB, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']