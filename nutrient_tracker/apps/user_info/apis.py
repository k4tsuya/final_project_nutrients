"""API views for user-related operations."""

from apps.tracker_data.models import NutrientTracker
from apps.user_info.models import User
from apps.user_info.serializers import (
    FavoriteSerializer,
    HistorySerializer,
    TrackedNutrientsSerializer,
    UserSerializer,
)
from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):
    """View for user information."""

    serializer_class = UserSerializer

    def get_permissions(self) -> list:
        """Return the list of permissions that this view requires."""
        self.permission_classes: list = [IsAdminUser]
        if self.request.method == "POST":
            self.permission_classes = [AllowAny]
        if self.request.method in {"PUT", "DELETE", "PATCH", "UPDATE"}:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    # READ
    def get(self, request: Request) -> Response:
        """Retrieve a list of all users."""
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    # CREATE
    def post(self, request: Request) -> Response:
        """Create a new user."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # UPDATE
    def update(self, request: Request, pk: int) -> Response:
        """Retrieve a specific user and update it."""
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request: Request, pk) -> Response:
        """Delete a specific user."""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailView(APIView):
    """View to retrieve, update, and delete a specific user."""

    serializer_class = UserSerializer

    def get_permissions(self) -> list:
        """Return the list of permissions required for this view."""
        self.permission_classes = [IsAuthenticated]
        if self.request.method in {"PUT", "DELETE", "PATCH", "UPDATE"}:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def get(self, request: Request, pk: int) -> Response:
        """Retrieve a specific user."""
        request_user = request.user
        user = User.objects.get(pk=pk)
        if request_user.is_superuser:
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        if request_user != user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            serializer = self.serializer_class(user)
            return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        """Update a specific user."""
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        """Delete a specific user."""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, pk: int) -> Response:
        """Partial update a specific user."""
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO Test the API views below.
class UserHistoryView(APIView):
    """View to handle history operations for a specific user."""

    serializer_class = HistorySerializer

    def get_permissions(self) -> list:
        """Return the list of permissions required for this view."""
        self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get(self, request: Request, pk: int) -> Response:
        """Retrieve the history of a specific user."""
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user.history)
        return Response(serializer.data)


class UserFavoriteView(APIView):
    serializer_class = FavoriteSerializer

    def get_permissions(self) -> list:
        """Return the list of permissions required for this view."""
        self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get(self, request: Request, pk: int) -> Response:
        """Retrieve the favorite items of a specific user."""
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user.favorite)
        return Response(serializer.data)


class TrackedNutrientsView(APIView):
    """Return the list of tracked nutrients for a specific user."""

    serializer_class = TrackedNutrientsSerializer

    def get_permissions(self) -> list:
        """Return the list of permissions required for this view."""
        self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get(self, request: Request, pk: int) -> Response:
        """Retrieve the tracked nutrients for a specific user."""
        trackers = NutrientTracker.objects.filter(user_id=pk)
        serializer = self.serializer_class(trackers, many=True)
        return Response(serializer.data)
