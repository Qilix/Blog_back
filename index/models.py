from django.contrib.auth.models import AbstractUser
from django.db import models
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

    
class Quote(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    sub_only = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title