from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import Base


class User(Base, AbstractUser):
    real_name = models.CharField(_('real name'), max_length=150)

    class Meta:
        ordering = ('-created',)
