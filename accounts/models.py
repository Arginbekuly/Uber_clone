from django.db.models import(
    Model, 
    DateTimeField,
    CharField,
    DecimalField,
    BooleanField,
    CheckConstraint,
    ManyToManyField,
    Q,
)
from django.contrib.auth.models import Group, Permission
from typing import Any
from django.contrib.auth.models import AbstractUser

from abstracts.models import AbstractBaseModel
from constants.auth_constants import default_role,ROLE_CHOICES,ROLES_LIST

class Account(AbstractUser, AbstractBaseModel):
    """
    Custom user model extending AbstractUser and AbstractBaseModel.
    """
    
    groups = ManyToManyField(
        Group,
        related_name="accounts_set",
        blank=True,
        verbose_name="account groups",
    )
    
    user_permissions = ManyToManyField(
        Permission,
        related_name="accounts_permission_set",
        blank=True,
        verbose_name="account permissions",
    )
    
    
    
    ROLE_MAX_LENGTH = 50
    PHONE_NUMBER_MAX_LENGTH = 50
    
    role = CharField(
        max_length=ROLE_MAX_LENGTH,
        choices=ROLE_CHOICES,
        default=default_role,
    )
    phone_number = CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        null=True,
        blank=True,
    )
    
    rating = DecimalField(
        default=0.0,
        max_digits=3,
        decimal_places=2,
    )
    
    is_active = BooleanField(
        default=True,
    )
    
    class Meta:
        constraints = [
            CheckConstraint(check=Q(role__in=ROLES_LIST), name='valid_role_constraint'),
        ]
        