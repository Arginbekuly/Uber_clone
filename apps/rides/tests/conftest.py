# Python modules
import pytest

# Django modules
from django.urls import reverse
from django.contrib.auth import get_user_model

@pytest.fixture
def vehicle_getlist_or_create_url():
    return reverse("vehicle-list")

@pytest.fixture
def valid_vehicle_data():
    return {
        "model":"Subaru XXL",
        "license_plate":"KZ23208",
        "driver":45
    }