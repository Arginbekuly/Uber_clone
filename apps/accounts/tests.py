#Django import
from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()

@pytest.mark.django_db
def test_register_success():
    client = APIClient()

    data = {
        "email": "user@example.com",
        "password": "test12345"
    }

    response = client.post("/api/register/", data)
    assert response.status_code == 201
    assert User.objects.filter(email="user@example.com").exists()
