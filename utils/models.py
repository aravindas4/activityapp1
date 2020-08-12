import uuid

from django.db import models
from model_utils.models import TimeStampedModel


def get_uuid():
    uuid_ = str(uuid.uuid4()).upper().replace('-', '')[:9]
    return uuid_


class Base(TimeStampedModel):
    id = models.CharField(
        max_length=30, primary_key=True, default=get_uuid, editable=False)

    class Meta:
        abstract = True
