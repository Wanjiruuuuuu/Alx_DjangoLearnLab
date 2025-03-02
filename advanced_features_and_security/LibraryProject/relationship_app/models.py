from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "can_add_book"),
            ("can_change_book", "can_change_book"),
            ("can_delete_book", "can_delete_book"),
        ]


class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE, related_name="librarian"
    )

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    USER_ROLES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    )

    from django.conf import settings  # Import settings

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userprofile"
    )
    role = models.CharField(max_length=255, choices=USER_ROLES)

    def __str__(self):
        return self.user.username + " " + self.role

    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_profile, sender=User)

    def update_profile(sender, instance, created, **kwargs):
        if created is False:
            instance.userprofile.save()

    post_save.connect(update_profile, sender=User)
