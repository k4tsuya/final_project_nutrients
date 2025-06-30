from django.test import TestCase
from apps.user_info.serializers import UserSerializer
from apps.user_info.models import User


# Create your tests here.
class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_user_serializer(self):
        serializer = UserSerializer(self.user)
        self.assertEqual(serializer.data["username"], "testuser")
