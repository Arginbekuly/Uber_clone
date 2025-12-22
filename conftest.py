# Python modules
import pytest


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def user_model():
    from django.auth.contrib import get_user_model
    return get_user_model()
