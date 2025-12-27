# Python modules
from typing import (
    Optional,
    Any,
)

# Django REST Framework
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    EmailField,
    CharField
)
from rest_framework.exceptions import ValidationError as DRFValidationError

# Project modules
from apps.auths.models import CustomUser

# Django modules
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

User = get_user_model()

class UserBaseSerializer(ModelSerializer):
    """
    Base serializer for CustomUser instances.
    """

    class Meta:
        """
        Customize the serializer's metadata.
        """
        model = CustomUser
        fields = "__all__"


class UserLoginSerializer(Serializer):
    """
    Serializer for user login.
    """
    email = EmailField(
        required=True,
        max_length=CustomUser.EMAIL_MAX_LENGTH,
    )
    password = CharField(
        required=True,
        max_length=CustomUser.PASSWORD_MAX_LENGTH,
    )

    class Meta:
        """Customization of the Serializer metadata."""
        fields = (
            "email",
            "password",
        )

    def validate_email(self, value: str) -> str:
        """Validates the email field."""
        return value.lower()

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        """Validates the input data."""
        email: str = attrs["email"]
        password: str = attrs["password"]

        user: Optional[CustomUser] = CustomUser.objects.filter(email=email).first()
        if not user:
            raise DRFValidationError(
                detail={
                     "email": [f"User with email '{email}' does not exist."]
                }
            )

        if not user.check_password(raw_password=password):
            raise DRFValidationError(
                detail={
                    "password": ["Incorrect password"]
                }
            )

        attrs["user"] = user
        return super().validate(attrs)

class RegisterSerializer(UserBaseSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "phone_number", "password", "role", "full_name")

    def validate_password(self, value):
        try:
            validate_password(value)
        except DjangoValidationError as e:
            raise DRFValidationError({"password": list(e.messages)})
        return value

    def validate(self, attrs):
        email = attrs.get("email")
        phone = attrs.get("phone_number")

        if not email and not phone:
            raise DRFValidationError("Provide email or phone_number")
        
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserMeSerializer(UserBaseSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "phone_number", "first_name", "last_name", "is_active")

class UserListSerializer(UserBaseSerializer):
    """
    Serializer for gaining List of all users

    Args:
        UserBaseSerializer (_type_): _description_
    """
    class Meta:
        """
        Customize the serializer's metadata.
        """
        model = CustomUser
        fields = (
            "id",
            "full_name",
            "email",
            "phone_number",
            "role"
        )
