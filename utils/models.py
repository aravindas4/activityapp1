import uuid

from django.db import models
from model_utils.models import TimeStampedModel


def get_uuid():
    return str(uuid.uuid4()).upper()[:9]


class Base(TimeStampedModel):
    id = models.CharField(
        max_length=30, primary_key=True, default=get_uuid)

    class Meta:
        abstract = True
