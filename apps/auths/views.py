# Python modules
from typing import Any
from rest_framework_simplejwt.tokens import RefreshToken

# Django REST Framework
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request as DRFRequest
from rest_framework.response import Response as DRFResponse
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
# Project modules
from apps.auths.models import CustomUser
from apps.auths.serializers import (
    UserLoginSerializer,
    RegisterSerializer,
    UserListSerializer,
)
# Django modules
from django.db.models import QuerySet


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
    
    @action(
        methods=("POST",),
        detail=False,
        url_path="register",
        url_name="register",
        permission_classes=(AllowAny,)
    )
    def register(
        self,
        request:DRFRequest,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any]
        ) -> DRFResponse:
        """
        Handle user registration.

        Args:
            request (DRFRequest): _description_

        Returns:
            DRFResponse: _description_
        """
        
        serializer : RegisterSerializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: CustomUser = serializer.save()
        
        return DRFResponse(
            serializer.validated_data,
            status=HTTP_201_CREATED
        )

class UserManipulationViewSet(ViewSet):
    """
    ViewSet for modifications of user's data

    Args:
        ViewSet (_type_): _description_
    """
    
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, )
    
    
    def list(
        self,
        request:DRFRequest,
        *args:tuple[Any, ...],
        **kwargs:dict[str, Any]
    ) -> DRFResponse:
        """
        Handle GET requests to list users.

        Args:
            request (DRFRequest): _description_

        Returns:
            DRFResponse: _description_
        """
        role = request.query_params.get("role")
        all_users : QuerySet[CustomUser] = self.queryset
        if role:
            all_users = all_users.filter(role=role)
            
        serializer : UserListSerializer = UserListSerializer(
            all_users,
            many=True
        )
        
        return DRFResponse(
            data=serializer.data,
            status=HTTP_200_OK
        )
   
    @action(
        methods=["GET",],
        detail=True,
        url_name="me",
        url_path="me"
    )
    def get_user(
        self,
        request:DRFRequest,
        *args: tuple[Any, ...],
        **kwargs : dict[str, Any]
    ) -> DRFResponse:
        """
        View to get one particular user
        """
        try:
            user : CustomUser = CustomUser.objects.get(id=kwargs["pk"])
        except CustomUser.DoesNotExist:
            return DRFResponse(
                data={
                    "id": [f"User with id={kwargs['pk']} does not exist."]
                },
                status=HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request=request, obj=user)
            
        return DRFResponse(
            data=UserListSerializer(
                user,
                many=False
            ).data,
            status=HTTP_200_OK
        )