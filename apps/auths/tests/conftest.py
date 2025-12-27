# Python modules
import pytest

# Django modules
from django.urls import reverse
from django.contrib.auth import get_user_model

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
def existing_user(db, valid_registration_data):
    User = get_user_model()
    return User.objects.create_user(
        email=valid_registration_data["email"],
        password=valid_registration_data["password"],
        full_name=valid_registration_data["full_name"],
        role=valid_registration_data["role"],
        phone_number=valid_registration_data["phone_number"],
    )

@pytest.fixture
def register_url():
    return reverse("user-register")

@pytest.fixture
def login_url():
    return reverse("user-login")


@pytest.fixture
def existing_user(db):
    return User.objects.create_user(
        email="user1@example.com",
        password="Password123!",
        full_name="User One",
        role="default_user",
        phone_number="87010000001"
    )

@pytest.fixture
def another_user(db):
    return User.objects.create_user(
        email="user2@example.com",
        password="Password123!",
        full_name="User Two",
        role="admin",
        phone_number="87010000002"
    )

@pytest.fixture
def authenticated_client(api_client, existing_user):
    api_client.force_authenticate(user=existing_user)
    return api_client

@pytest.fixture
def user_list_url():
    return reverse("user-list")

@pytest.fixture
def user_detail_url(existing_user):
    return reverse("user-detail", kwargs={"pk": existing_user.id})