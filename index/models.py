from django.contrib.auth.models import AbstractUser
from django.db import models

from users.models import User


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    sub_only = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title