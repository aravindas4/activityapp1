from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.prefetch_related(
        'activity_periods'
    )
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='activity')
    def get_user_activity(self, request, *args, **kwargs):
        '''
        Returns all users and thier respective activities' details
        input: None
        output: {
            "ok": true,
            "members": [
                {
                    "id": "8567153BD",
                    "real_name": "Glinda Southgood",
                    "tz": "Asia/Kolkata",
                    "activity_periods": [
                        {
                            "start_time": "Aug 12 2020  04:15AM",
                            "end_time": "Aug 12 2020  05:15AM"
                        },
                        {
                            "start_time": "Sep 12 2020  04:15AM",
                            "end_time": "Sep 12 2020  05:15AM"
                        },
                        {
                            "start_time": "Oct 12 2020  04:15AM",
                            "end_time": "Oct 12 2020  05:15AM"
                        }
                    ]
                }
            ]
        }
        '''
        response = {
            "ok": False
        }

        queryset = self.get_queryset()
        if queryset.exists():
            response.update({
                "ok": True,
                "members": self.get_serializer(queryset, many=True).data
            })

        return Response(response)
