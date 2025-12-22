# Python modules
import pytest

# Django modules
from django.contrib.auth import get_user_model
from django.urls import reverse

# Django REST Framework
from rest_framework.status import HTTP_201_CREATED


@pytest.mark.django_db
def test_successful_registration(api_client, valid_registration_data, register_url):
    """
    + Positive test -> user successfully can be created by API
    """

    print("current url:", register_url)

    response = api_client.post(register_url, valid_registration_data, format="json")

    assert response.status_code == HTTP_201_CREATED
