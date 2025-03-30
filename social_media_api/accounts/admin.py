from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["username", "email", "first_name", "last_name", "is_staff"]
    fieldsets = (
        (
            None,
            {
                "fields": ["email", "username", "bio", "profile_picture"],
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "email",
                    "username",
                    "bio",
                    "profile_picture",
                    "is_staff",
                    "password1",
                    "password2",
                ]
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)