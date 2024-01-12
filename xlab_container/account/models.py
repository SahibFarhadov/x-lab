from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import AuthorManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Author(AbstractUser):
    username = None
    email = models.EmailField(_("Email"),unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = AuthorManager()
    def __str__(self):
        return self.email