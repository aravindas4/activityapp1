from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='activity')
    def get_user_activity(self, request, *args, **kwargs):
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
