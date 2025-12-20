#Django modules
from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    PositiveIntegerField,
    DateTimeField,
    CASCADE,
    SET_NULL
)
from django.contrib.auth import get_user_model

# Application modules
from apps.autopark.models import AutoPark

User = get_user_model()

class Vehicle(Model):
    """
    Vehicle driven by a driver.

    driver : owner of the vehicle
    model: vehicle model
    license_plate: license number
    capacity: number of passengers
    """
    driver = ForeignKey(User,on_delete=CASCADE, related_name= "vehicles")
    model = CharField(max_length = 100)
    license_plate = CharField(max_length = 20, unique=True)
    capacity = PositiveIntegerField(default = 4)
    autopark = ForeignKey(
        "autopark.AutoPark",
        on_delete=CASCADE,
        related_name="vehicles",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{ self.model } ({self.license_plate})"
    

class Ride(Model):
    """
    Ride request in the system.

    driver: the driver
    passenger: the passenger
    start_loc = where it starts
    end_loc = where it ends
    status: requested,accepted, in progress,completed or cancelled
    created_at : when the ride was created
    """
    STATUS_CHOISES = [
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('in_progres', 'In Progres'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    driver = ForeignKey(User, on_delete=SET_NULL, null=True, related_name = 'rides_as_driver')
    passenger = ForeignKey(User, on_delete=SET_NULL, null = True, related_name='rides_as_passenger')
    start_location = CharField(max_length = 100)
    end_location = CharField(max_length = 100)
    status = CharField(max_length = 20, choices= STATUS_CHOISES, default= 'requested')
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride { self.id }: { self.start_location } -> { self.end_location } ({ self.status })"
