from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User should an email.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = models.CharField(unique=False, max_length=100)
    email = models.EmailField(unique=True, max_length=200)
    bio = models.TextField(max_length=255)
    profile_picture = models.ImageField(upload_to="images")
    followers = models.ManyToManyField("self", symmetrical=False)
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="following"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()