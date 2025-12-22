# Python modules
import pytest

# Django modules
from django.urls import reverse

@pytest.fixture
def valid_registration_data():
    return {
        "email": "testik@example.com",
        "password": "12345678Aa",
        "full_name": "Palensheev Palenshe",
        "role": "default_user",
        "phone_number": "87012133212",
    } 

@pytest.fixture
def register_url():
    return reverse("user-register")

