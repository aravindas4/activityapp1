from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from timezone_field import TimeZoneField

from utils.models import Base


class User(Base, AbstractUser):
    real_name = models.CharField(_('real name'), max_length=150)
    tz = TimeZoneField(_('timezone'), default='Asia/Kolkata')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.real_name}'


class ActivityPeriod(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="activity_periods")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        ordering = ('created',)
