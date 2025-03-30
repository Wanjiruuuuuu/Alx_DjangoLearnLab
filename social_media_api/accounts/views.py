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



class CustomUserListAPIView(generics.GenericAPIView, generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
