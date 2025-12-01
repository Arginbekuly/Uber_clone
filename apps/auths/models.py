#Python modules
from typing import Any

#Django modules
from django.db.models import (
    EmailField,
    CharField,
    BooleanField,
)
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


#Project modules
from apps.abstracts.models import AbstractBaseModel


class CustomUserManager(BaseUserManager):
    """Custom User Manager to make db requests."""

    def __obtain_user_instance(
        self,
        email: str,
        full_name : str,
        password: str,
        **kwargs: dict[str, Any], 
        ) -> 'CustomUser':
        """Get user instance."""
        if not email:
            raise ValidationError(
                message = "Email field is required.",code = "email_empty" 
            )
        new_user: 'CustomUser' = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
            password = password,
            **kwargs,
        )
        return new_user

    def create_user(
        self,
        email: str,
        full_name : str,
        password: str,
        **kwargs: dict[str, Any], 
        ) -> 'CustomUser':
        """Create Custom User. TODO where is this used"""
        new_user: 'CustomUser' = self.__obtain_user_instance(
            email = email,
            full_name = full_name,
            password = password,
            **kwargs,
        )
        new_user.set_password(password)
        new_user.save(using = self._db)
        return new_user

    def create_superuser(
            self,
            email: str,
            full_name : str,
            password: str,
            **kwargs: dict[str, Any], 
        ) -> 'CustomUser':
        """Create Custom User. TODO where is this used"""
        new_user: 'CustomUser' = self.__obtain_user_instance(
            email = email,
            full_name = full_name,
            password = password,
            **kwargs,
        )
        new_user.set_password(password)
        new_user.save(using = self._db)
        return new_user
    
class CustomUser(AbstractBaseUser,AbstractBaseModel,PermissionsMixin):
    """Custom user model existions Abstract Base Model."""
    EMAIL_MAX_LENGTH = 128
    FULL_NAME_MAX_LENGTH = 128
    PASSWORD_MAX_LENGTH = 254

    email = EmailField(
        max_length = EMAIL_MAX_LENGTH,
        unique = True,
        db_index = True,
        verbose_name = "Email address",
        help_text = "User`s email address",
    )
    full_name = CharField(
        max_length = FULL_NAME_MAX_LENGTH,
        verbose_name = "Full name",
        help_text = "User`s full name",
    )
    password = CharField(
        max_length = PASSWORD_MAX_LENGTH,
        validators = [validate_password],
        verbose_name = "Password",
        help_text = "User`s hash representation of the password",
    )
    phone_number = CharField(
        max_length = 20,
        verbose_name = "Phone number",
        help_text = "User`s phone number"
    )
    is_staff = BooleanField(
        default = False,
        verbose_name = "Staff status",
        help_text = "True if the user is an admin  and has an access to the admin panel",
    )
    is_active = BooleanField(
        default = True,
        verbose_name = "Active status",
        help_text = "True if the user is active and has an access to request to data",
    )
    REQUIRED_FIELDS = ["full_name"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    class Meta:
        """Meta options for CustomUser model."""

        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
        ordering = ["-created_at"]
