#Django imports
from django.urls import path
from .views import RegisterAPIView, UserMeAPIView

#Django URL patterns
urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("user/me/", UserMeAPIView.as_view(), name="user-me"),
]
