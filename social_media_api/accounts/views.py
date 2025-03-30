from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from django.contrib.auth.models import User

# serializers
from .serializers import (
    CustomUserRegistrationSerializer,
    CustomUserLoginSerializer,
    CustomUserSerializer,
)


# Create your views here.
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
            }
        )


class CustomUserLoginApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                "email": {"detail": "User does not exist"},
            }

            if get_user_model().objects.filter(email=request.data["email"]).exists():
                user = get_user_model().objects.get(email=request.data["email"])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    "successful": True,
                    "email": user.email,
                    "token": token.key,
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserRegistrationApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "successful": True,
                "user": serializer.data,
                "token": Token.objects.get(
                    user=get_user_model().objects.get(email=serializer.data["email"])
                ).key,
            }
            return Response(response, status=status.HTTP_200_OK)
        raise ValidationError(serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)


class CustomUserLogoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        response = {
            "success": True,
            "detail": "Logged out.",
        }
        return Response(response, status=status.HTTP_200_OK)


# The REST_FRAMEWORK settings should be moved to settings.py


class CustomUserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Follow and Unfollow Views
class FollowUserView(APIView):
    """
    Allows a user to follow another user.
    Authentication is manually checked instead of using `permissions.IsAuthenticated`.
    """
    def post(self, request, username):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user_to_follow = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        profile = request.user.profile  # Assuming a OneToOne field in Profile linked to User
        if user_to_follow in profile.following.all():
            return Response({"message": "Already following this user"}, status=status.HTTP_400_BAD_REQUEST)

        profile.following.add(user_to_follow)
        return Response({"message": f"You are now following {username}"}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    """
    Allows a user to unfollow another user.
    """
    def post(self, request, username):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user_to_unfollow = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        profile = request.user.profile
        if user_to_unfollow not in profile.following.all():
            return Response({"message": "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)

        profile.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {username}"}, status=status.HTTP_200_OK)
