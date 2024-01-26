from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import AuthorManager
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class Author(AbstractUser):
    class Meta:
        verbose_name = 'Müəllif'
        verbose_name_plural = 'Müəlliflər'
    username = None
    email = models.EmailField(_("Email"),unique=True)
    author_uuid = models.UUIDField(editable=False,null=True,default=uuid.uuid4)
    email_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = AuthorManager()
    
    def __str__(self):
        return self.email

    def save(self,*args,**kwargs):
        self.author_uuid = uuid.uuid4()
        super().save(*args,**kwargs)