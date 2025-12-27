# Python modules
import pytest

# Django modules
from django.contrib.auth import get_user_model
from django.urls import reverse

# Django REST Framework
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)


@pytest.mark.django_db
def test_successful_registration(api_client, valid_registration_data, register_url):
    """
    + Positive test -> user successfully can be created by API
    """

    response = api_client.post(register_url, valid_registration_data, format="json")

    assert response.status_code == HTTP_201_CREATED


@pytest.mark.django_db
def test_user_already_exists(api_client, existing_user, valid_registration_data, register_url):
    """
    - Negative test -> the case of existing of user when you try to register new one
    """

    response = api_client.post(register_url, valid_registration_data, format="json")
    
    assert response.status_code == HTTP_400_BAD_REQUEST


@pytest.mark.django_db  
def test_required_field_not_provided(api_client, valid_registration_data, register_url):
    """
    - Negative test -> trying to register user but not provided all required fields
    """
    insufficient_data = {k : v for k, v in valid_registration_data.items() if k != "email"}
    response = api_client.post(register_url, insufficient_data, format="json")

    assert response.status_code == HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_password_too_weak(api_client, valid_registration_data, register_url):
    """
    - Negative test -> trying to register user with weak password
    """
    
    weak_password_data = dict(valid_registration_data)
    weak_password_data["password"] = "12345"

    response = api_client.post(register_url, weak_password_data, format="json")

    assert response.status_code == HTTP_400_BAD_REQUEST
    
    assert "password" in response.data
