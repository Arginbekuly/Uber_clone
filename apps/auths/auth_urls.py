# Django Rest Framework modules
from rest_framework.routers import DefaultRouter

# Project modules
from apps.auths.views import CustomUserViewSet

router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)

router.register(
    prefix="users",
    viewset=CustomUserViewSet,
    basename="user",
)

urlpatterns = router.urls
