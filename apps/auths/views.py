# Python modules
from typing import Any
from rest_framework_simplejwt.tokens import RefreshToken

# Django REST Framework
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request as DRFRequest
from rest_framework.response import Response as DRFResponse
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

# Project modules
from apps.auths.models import CustomUser
from apps.auths.serializers import UserLoginSerializer

class CustomUserViewSet(ViewSet):
    """
    ViewSet for handling CustomUser-related endpoints.
    """
    @action(
        methods=("POST",),
        detail=False,
        url_path="login",
        url_name="login",
        permission_classes=(AllowAny,)
    )
    def login(
        self,
        request : DRFRequest,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any]
    ) -> DRFResponse:
        """
        Handle user login.

        Parameters:
            request: DRFRequest
                The request object.
            *args: tuple
                Additional positional arguments.
            **kwargs: dict
                Additional keyword arguments.

        Returns:
            DRFResponse
                Response containing user data or error message.
        """
        serializer : UserLoginSerializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user:CustomUser = serializer._validated_data.pop("user")
        
        refresh_token : RefreshToken = RefreshToken.for_user(user)
        access_token : str = str(refresh_token.access_token)
        
        return DRFResponse(
            data={
                 "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "access": access_token,
                "refresh": str(refresh_token),
            },
            status=HTTP_200_OK
        )
    
    