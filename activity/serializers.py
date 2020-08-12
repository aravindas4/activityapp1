from utils.serializers import BaseSerializer

from .models import ActivityPeriod, User


class ActivityPeriodSerializer(BaseSerializer):

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserSerializer(BaseSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')
