from utils.models import get_uuid
from utils.serializers import BaseSerializer, TimeZoneField

from .models import ActivityPeriod, User


class ActivityPeriodSerializer(BaseSerializer):

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserSerializer(BaseSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)
    tz = TimeZoneField()

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')

    def create(self, validated_data):
        validated_data['username'] = validated_data['id'] = get_uuid()
        return super().create(validated_data)
