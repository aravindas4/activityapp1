from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from timezone_field import TimeZoneField as TimeZoneField_


class BaseSerializer(WritableNestedModelSerializer):
    pass


class TimeZoneField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        super().__init__(TimeZoneField_.CHOICES + [(None, "")], **kwargs)

    def to_representation(self, value):
        return str(super().to_representation(value))
