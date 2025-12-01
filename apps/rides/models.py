#Django modules
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Vehicle(models.Model):
    """
    Vehicle driven by a driver.

    driver : owner of the vehicle
    model: vehicle model
    license_plate: license number
    capacity: number of passengers
    """
    driver = models.ForeignKey(User,on_delete=models.CASCADE, related_name= "vehicles")
    model = models.CharField(max_length = 100)
    license_plate = models.CharField(max_length = 20, unique=True)
    capacity =models.PositiveIntegerField(default = 4)

    def __str__(self):
        return f"{ self.model } ({self.license_plate})"
    

class Ride(models.Model):
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

    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name = 'rides_as_driver')
    passenger = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, related_name='rides_as_passenger')
    start_location = models.CharField(max_length = 100)
    end_location = models.CharField(max_length = 100)
    status = models.CharField(max_length = 20, choices= STATUS_CHOISES, default= 'requested')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride { self.id }: { self.start_location } -> { self.end_location } ({ self.status })"
