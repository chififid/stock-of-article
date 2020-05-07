from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import datetime, timedelta

class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Activate(models.Model):
    email = models.EmailField()
    key = models.IntegerField(unique=True)
    activate = models.BooleanField(null=True, blank=True, default=False)
    password = models.CharField(max_length=150, blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    def __str__(self):
        a = datetime.now()
        b = timedelta(minutes=20)
        if a.replace(tzinfo=None) - self.published.replace(tzinfo=None) >= b:
            self.delete()
        else:
            return str(self.key)

    class Meta:
        verbose_name = 'Активация'
        verbose_name_plural = 'Активации'
