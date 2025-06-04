import json
from pathlib import Path

from apps.user_info.models import User
from apps.tracker_data.models import NutrientTracker
from apps.user_info.serializers import (
    UserSerializer,
    HistorySerializer,
    FavoriteSerializer,
    TrackedNutrientsSerializer,
)
from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):
    serializer_class = UserSerializer

    # READ
    def get(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    # CREATE
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # UPDATE
    def update(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailView(APIView):
    serializer_class = UserSerializer

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserHistoryView(APIView):
    serializer_class = HistorySerializer

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user.history)
        return Response(serializer.data)


class UserFavoriteView(APIView):
    serializer_class = FavoriteSerializer

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user.favorite)
        return Response(serializer.data)


class TrackedNutrientsView(APIView):
    serializer_class = TrackedNutrientsSerializer

    def get(self, request, pk):
        trackers = NutrientTracker.objects.filter(user_id=pk)
        serializer = self.serializer_class(trackers, many=True)
        return Response(serializer.data)
