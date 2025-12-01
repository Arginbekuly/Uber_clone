# Django modules
from django.db.models import (
    TextChoices,
    CharField,
    EmailField,
    DateField,
    BooleanField,
    DateTimeField
)
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    
    Это кастомный класс пользователей, который можно расширять.

    Args:
        AbstractBaseUser (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    class Roles(TextChoices):
        ADMIN = "admin", "Admin",
        DRIVER = "driver", "Driver"
        PASSENGER_CLIENT = "passenger_client", "Passenger_Client"
        OPERATOR = "operator", "Operator"
        DEFAULT_USER = "default_user", "Default_User"
    
    email = EmailField(unique=True)
    first_name = CharField(max_length=30, blank=True)
    last_name = CharField(max_length=30, blank=True)
    phone = CharField(max_length=15, blank=True)
    city = CharField(max_length=15, blank=True)
    country = CharField(max_length=15, blank=True)
    role = CharField(max_length=10, choices=Roles.choices, default=Roles.DEFAULT_USER)
    birth_date = DateField(null=True, blank=True)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    date_joined = DateTimeField(auto_now_add=True, editable=False)
    last_login = DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email',
    REQUIRED_FIELDS = ['email', 'role',]
    
    def __str__(self):
        return f"User with email {self.email}"