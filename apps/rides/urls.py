#Django modules
from django.urls import path

#Django rest framework
from rest_framework.routers import DefaultRouter

#Project modules
from .views import RideViewSet, VehicleViewSet


router : DefaultRouter = DefaultRouter(
    trailing_slash=False
)

router.register(
    prefix="trip",
    viewset=RideViewSet, 
    basename = "ride"
)

router.register(
    prefix="vehicles", 
    viewset=VehicleViewSet,
    basename = "vehicle"
)

urlpatterns = router.urls