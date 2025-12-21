from django.db.models import Model, DateTimeField
from typing import Any
from django.utils import timezone as django_timezone


# Create your models here.
class AbstractBaseModel(Model):
    """
    Abstract base model with common fields.

    created_at : when record was created
    updated_at : when record was updated
    deleted_at : when record was deleted
    """
    created_at = DateTimeField(
        auto_now_add=True,
    )
    updated_at = DateTimeField(
        auto_now=True,
    )
    deleted_at = DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        """Meta class"""
        abstract = True

    def delete(self,*args:tuple[Any, ...], **kwargs:dict[str, Any]) -> None:
        """
        
        """
        self.deleted_at = django_timezone.now()
        self.save(update_fields=['deleted_at'])
