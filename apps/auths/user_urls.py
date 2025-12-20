# Django Rest Framework modules
from rest_framework.routers import DefaultRouter

# Project modules
from apps.auths.views import UserManipulationViewSet

router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)

router.register(
    prefix="",
    viewset=UserManipulationViewSet,
    basename="user"
)

urlpatterns = router.urls
