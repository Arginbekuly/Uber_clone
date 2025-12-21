# Python modules

# Django modules
from django.test import TestCase
from django.contrib.auth import get_user_model

# Project modules

# Django REST Framework
from rest_framework.status import HTTP_201_CREATED

User = get_user_model()

# class VehicleModelTest(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='driver1',
#             email='driver1@example.com',
#             full_name='Driver One',
#             role='driver',
#             password='pass1234'
#         )

#     def test_create_vehicle_success(self):
#         vehicle = Vehicle.objects.create(
#             driver=self.user,
#             model='Toyota Corolla',
#             license_plate='ABC123',
#             capacity=4
#         )
#         self.assertEqual(vehicle.model, 'Toyota Corolla')
#         self.assertEqual(vehicle.capacity, 4)
#         self.assertEqual(vehicle.driver.username, 'driver1')

#     def test_vehicle_str(self):
#         vehicle = Vehicle.objects.create(
#             driver=self.user,
#             model='Honda Civic',
#             license_plate='XYZ789'
#         )
#         self.assertEqual(str(vehicle), 'Honda Civic (XYZ789)')

#     def test_vehicle_license_plate_unique(self):
#         Vehicle.objects.create(driver=self.user, model='Toyota', license_plate='DUP123')
#         with self.assertRaises(Exception):
#             Vehicle.objects.create(driver=self.user, model='Honda', license_plate='DUP123')


class RideModelTest(TestCase):

    def setUp(self):
        self.driver = User.objects.create_user(
            email='driver1123123123@example.com',
            full_name='Driver One',
            role='driver',
            password='pass1234',
            phone_number='87771221222'
        )
        self.passenger = User.objects.create_user(
            email='passenger121231231231@example.com',
            full_name='Passenger One',
            role='passenger',
            password='pass1234',
            phone_number='87771221224'
        )

    def test_create_ride_success(self):
        url = "/api/rides/trip"
        data = {
            "driver":self.driver.id,
            "passenger":self.passenger.id,
            "start_location":"A",
            "end_location":"B",
            "status":"in_progres",
            "created_at": "2025-12-09T10:21:00+05:00"
        }
        response = self.client.post(url, data, format="json")

        if response.status_code != 201:
            print("Response errors:", response.data)

        self.assertEqual(response.status_code, HTTP_201_CREATED)

        # self.assertEqual(ride.passenger.username, 'passenger1')

    # def test_ride_str(self):
    #     ride = Ride.objects.create(
    #         driver=self.driver,
    #         passenger=self.passenger,
    #         start_location='City Center',
    #         end_location='Airport'
    #     )
    #     self.assertIn('City Center -> Airport', str(ride))

    # def test_ride_status_invalid(self):
    #     with self.assertRaises(ValueError):
    #         Ride.objects.create(
    #             driver=self.driver,
    #             passenger=self.passenger,
    #             start_location='A',
    #             end_location='B',
    #             status='unknown_status'
    #         )
