#Django modules
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model

#Prpject modules
from apps.rides.models import Vehicle, Ride

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate database with test users, vehicles, and rides'

    def handle(self, *args, **options):
        self.stdout.write('Creating users...')
        """Create two driver with passenger and rides for db"""
        driver1 = User.objects.create_user(
            email='driver1@example.com',
            full_name='Driver One',
            role='driver',
            password='pass1234'
        )
        driver2 = User.objects.create_user(
            email='driver2@example.com',
            full_name='Driver Two',
            role='driver',
            password='pass1234'
        )

        
        passenger1 = User.objects.create_user(
            email='passenger1@example.com',
            full_name='Passenger One',
            role='passenger_client',
            password='pass1234'
        )
        passenger2 = User.objects.create_user(
            email='passenger2@example.com',
            full_name='Passenger Two',
            role='passenger_client',
            password='pass1234'
        )

        self.stdout.write('Creating vehicles...')
        vehicle1 = Vehicle.objects.create(
            driver=driver1,
            model='Toyota Corolla',
            license_plate='ABC123',
            capacity=4
        )
        vehicle2 = Vehicle.objects.create(
            driver=driver2,
            model='Honda Civic',
            license_plate='XYZ789',
            capacity=4
        )

        self.stdout.write('Creating rides...')
        Ride.objects.create(
            driver=driver1,
            passenger=passenger1,
            start_location='City Center',
            end_location='Airport',
            status='requested',
            created_at=timezone.now()
        )
        Ride.objects.create(
            driver=driver2,
            passenger=passenger2,
            start_location='Train Station',
            end_location='Mall',
            status='accepted',
            created_at=timezone.now()
        )

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))