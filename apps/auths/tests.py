# Python modules

#Django modules
from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED


class RegistrationTestCase(APITestCase):
    User = get_user_model()

    def test_successful_registration(self):
        """
        Проверяет, что пользователь успешно создаётся через API.
        """

        url = "/api/auths/users/register"

        data = {
            "email": "testik@example.com",
            "password": "12345678Aa",
            "full_name": "Palensheev Palenshe",
            "role": "default_user",
            "phone_number":"87012133212"
        }

        response = self.client.post(url, data, format="json")

        if response.status_code != 201:
            print("Response errors:", response.data)

        self.assertEqual(response.status_code, HTTP_201_CREATED)

        user_exists = self.User.objects.filter(email="testik@example.com").exists()
        self.assertTrue(user_exists)
