#Django modules
from django.contrib import admin

#Project modules
from .models import Vehicle, Ride
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """Admin settings for Vehicle"""
    list_display = ('model', 'license_plate', 'driver', 'capacity')
    search_fields = ('license_plate','model', 'driver__username')

    
@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    """Admin settings for Ride"""
    list_display = ('id', 'driver' ,'passenger', 'start_location', 'end_location', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('start_location', 'end_location', 'driver__username', 'passenger__username')