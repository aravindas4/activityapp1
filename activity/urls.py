from rest_framework.routers import SimpleRouter

from .api import UserModelViewSet

router = SimpleRouter()

router.register(r'', UserModelViewSet, basename='user')


urlpatterns = router.urls
