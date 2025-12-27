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
def test_list_users(authenticated_client, user_list_url, existing_user, another_user):
    """
    + Positive test -> successfully retrieve a list of all users
    """
    response = authenticated_client.get(user_list_url)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 2


@pytest.mark.django_db
def test_list_users_filtered_by_role(authenticated_client, user_list_url, existing_user, another_user):
    """
    + Positive test -> successfully retrieve a list of users filtered by role
    """
    response = authenticated_client.get(user_list_url, {"role": "admin"})
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["email"] == another_user.email


@pytest.mark.django_db
def test_get_user_success(authenticated_client, user_detail_url, existing_user):
    """
    + Positive test -> successfully retrieve a single user by ID
    """
    response = authenticated_client.get(user_detail_url)
    assert response.status_code == HTTP_200_OK
    assert response.data["email"] == existing_user.email


@pytest.mark.django_db
def test_get_user_not_found(authenticated_client):
    """
    - Negative test -> attempt to retrieve a user that does not exist returns 404
    """
    url = reverse("user-detail", kwargs={"pk": 999})
    response = authenticated_client.get(url)
    assert response.status_code == HTTP_404_NOT_FOUND
    assert "id" in response.data


@pytest.mark.django_db
def test_list_users_unauthenticated(api_client, user_list_url):
    """
    - Negative test -> unauthenticated request to list users is forbidden
    """
    response = api_client.get(user_list_url)
    assert response.status_code == HTTP_403_FORBIDDEN