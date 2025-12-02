#Django imports
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.request import Request
from accounts.permissions import IsAdminUser, IsOwner, BanManagementPermission

# Create your tests.
User = get_user_model()

class TestIsAdminUser(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(email="admin@test.com", password="12345", is_staff=True)
        self.user = User.objects.create_user(email="user@test.com", password="12345")

    def test_admin_has_permission(self):
        self.client.force_authenticate(self.admin)
        request = APIRequestFactory().get("/")
        request.user = self.admin

        permission = IsAdminUser()
        self.assertTrue(permission.has_permission(request, None))

    def test_user_denied(self):
        request = APIRequestFactory().get("/")
        request.user = self.user

        permission = IsAdminUser()
        self.assertFalse(permission.has_permission(request, None))

class TestIsOwner(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="a@test.com", password="pass")
        self.other = User.objects.create_user(email="b@test.com", password="pass")

    def test_owner_has_access(self):
        request = APIRequestFactory().get("/")
        request.user = self.user
        perm = IsOwner()

        self.assertTrue(perm.has_object_permission(request, None, self.user))

    def test_not_owner_denied(self):
        request = APIRequestFactory().get("/")
        request.user = self.user
        perm = IsOwner()

        self.assertFalse(perm.has_object_permission(request, None, self.other))

class FakeView:
    action = None


class TestBanManagementPermission(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(email="admin@test.com", password="12345", is_staff=True)
        self.user = User.objects.create_user(email="user@test.com", password="12345")

    def test_admin_can_ban(self):
        view = FakeView()
        view.action = "ban"

        request = APIRequestFactory().post("/")
        request.user = self.admin

        perm = BanManagementPermission()
        self.assertTrue(perm.has_permission(request, view))

    def test_user_cannot_ban(self):
        view = FakeView()
        view.action = "ban"

        request = APIRequestFactory().post("/")
        request.user = self.user

        perm = BanManagementPermission()
        self.assertFalse(perm.has_permission(request, view))

    def test_user_can_other_actions(self):
        view = FakeView()
        view.action = "list"  # open action

        request = APIRequestFactory().get("/")
        request.user = self.user

        perm = BanManagementPermission()
        self.assertTrue(perm.has_permission(request, view))
