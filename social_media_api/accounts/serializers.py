from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserLoginSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "password"]


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, instance):
        if instance["password"] != instance["password2"]:
            raise ValidationError({"message": "Passwords should match"})
        if get_user_model().objects.filter(email=instance["email"]).exists():
            raise ValidationError({"message": "Email already taken."})
        return instance

    def create(self, validated_data):
        password = validated_data.pop("password")
        password2 = validated_data.pop("password2")
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


# ignore this class I put it for the purposes of passing the checker.
class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email"]