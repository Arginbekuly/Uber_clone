#Django modules
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Vehicle(models.Model):
    driver = models.ForeignKey(User,on_delete=models.CASCADE, related_name= "vehicles")
    model = models.CharField(max_length = 100)
    licence_plate = models.CharField(max_length = 20, unique=True)
    capacity =models.PositiveIntegerField(default = 4)

    def __str__(self):
        return f"{ self.model } ({self.licence_plate})"
    

class Ride(models.Model):
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
