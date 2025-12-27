# Python modules
import pytest

# Django modules
from django.contrib.auth import get_user_model
from django.urls import reverse

# Django REST Framework
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

@pytest.mark.django_db
def test_success_vehicle_create(api_client, vehicle_getlist_or_create_url, valid_vehicle_data):
    """
    + Positive test -> Success Vehicle creation by API
    """
    
    response = api_client.post(vehicle_getlist_or_create_url, valid_vehicle_data, format="json")
    assert response.status_code == HTTP_201_CREATED


@pytest.mark.django_db
def test_vehicle_missing_required_field(api_client, vehicle_getlist_or_create_url, valid_vehicle_data):
    """
    - Negative test -> missing required field 'model'
    """
    invalid_data = dict(valid_vehicle_data)
    invalid_data.pop("model")  
    response = api_client.post(vehicle_getlist_or_create_url, invalid_data, format="json")

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert "model" in response.data


@pytest.mark.django_db
def test_vehicle_invalid_field_type(api_client, vehicle_getlist_or_create_url, valid_vehicle_data):
    """
    - Negative test -> invalid field type for 'driver'
    """
    invalid_data = dict(valid_vehicle_data)
    invalid_data["driver"] = "not_a_number"
    response = api_client.post(vehicle_getlist_or_create_url, invalid_data, format="json")

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert "driver" in response.data


@pytest.mark.django_db
def test_vehicle_duplicate_license_plate(api_client, vehicle_getlist_or_create_url, valid_vehicle_data):
    """
    - Negative test -> duplicate license_plate
    """
    
    response1 = api_client.post(vehicle_getlist_or_create_url, valid_vehicle_data, format="json")
    assert response1.status_code == HTTP_201_CREATED

    response2 = api_client.post(vehicle_getlist_or_create_url, valid_vehicle_data, format="json")
    assert response2.status_code == HTTP_400_BAD_REQUEST
    assert "license_plate" in response2.data