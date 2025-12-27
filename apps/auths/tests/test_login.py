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
def test_successful_login(api_client, existing_user, valid_registration_data, login_url):
    """
    + Positive test -> user can login with correct credentials
    """
    login_data = {
        "email": valid_registration_data["email"],
        "password": valid_registration_data["password"],
    }
    response = api_client.post(login_url, login_data, format="json")
    assert response.status_code == HTTP_200_OK
    assert "access" in response.data


@pytest.mark.django_db
def test_login_wrong_password(api_client, existing_user, valid_registration_data, login_url):
    """
    - Negative test -> login fails with incorrect password
    """
    login_data = {
        "email": valid_registration_data["email"],
        "password": "wrongpassword123",
    }
    response = api_client.post(login_url, login_data, format="json")
    assert response.status_code == HTTP_400_BAD_REQUEST or response.status_code == HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_login_nonexistent_user(api_client, login_url):
    """
    - Negative test -> login fails if user does not exist
    """
    login_data = {
        "email": "nonexistent@example.com",
        "password": "SomePassword123",
    }
    response = api_client.post(login_url, login_data, format="json")
    assert response.status_code == HTTP_400_BAD_REQUEST or response.status_code == HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
@pytest.mark.parametrize(
    "missing_field_data",
    [
        ({"password": "12345678Aa"}),
        ({"email": "testik@example.com"}),
        ({})  # missing both
    ]
)
def test_login_missing_required_fields(api_client, missing_field_data, login_url):
    """
    - Negative test -> login fails if required fields are missing
    """
    response = api_client.post(login_url, missing_field_data, format="json")
    assert response.status_code == HTTP_400_BAD_REQUEST