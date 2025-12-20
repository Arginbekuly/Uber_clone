#Python modules
from typing import Any

#Rest framework modules
from rest_framework.serializers import (
    Serializer, 
    IntegerField, 
    CharField,
    ModelSerializer
)
from rest_framework.validators import ValidationError

#Project modules
from .models import Ride, Vehicle


class VehicleSerializer(ModelSerializer):
    """
    Serializer for the Vehicle
    """

    class Meta:
        """
        Meta class Vehicle
        """
        
        model = Vehicle
        fields = "__all__"
    
    def validate_capacity(self, value):
        """
        Validate that vehicle capacity is at least 1.

        Args:
            value(int):The capacity of the vehicle.

        Returns:
            int: Validated capacity.
        """
        
        if value < 1:
            raise ValidationError("Capaicty must be at least 1.")
        return value


class RideSerializer(ModelSerializer):
    """
    Serializer for the Ride.
    """
    
    class Meta:
        """
        meta class Ride
        """
        
        model = Ride
        fields = "__all__"

    def validate_status(self, value: str) -> str:
        """
        Validate that status is one of the allowed choices.

        Args:
            value(str):Status of the ride.

        Returns:
            str: Validated status.
        """
        
        if value not in dict(Ride.STATUS_CHOISES):
            raise ValidationError("Invalid Error!")
        return value
    
    def validate_user(self, data: dict[str, Any])-> dict[str, Any]:
        """
        Ensures that driver and passenger are not the same.

        Args:
            data(Dict[str, Any]):All input data.

        Returns:
            Dict[str, Any]:Validated data.
        """
        
        if data.get("driver") == data.get("passenger"):
            raise ValidationError("Driver cannot be passenger.")
        return data