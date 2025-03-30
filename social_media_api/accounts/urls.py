from django.urls import path
from rest_framework.authtoken import views
from .views import (
    CustomAuthToken,
    CustomUserLoginApiView,
    CustomUserRegistrationApiView,
    CustomUserLogoutApiView,
    FollowUserView,  # Importing the missing view
    UnfollowUserView,  # Importing the missing view
)


urlpatterns = [
    path("login/", CustomUserLoginApiView.as_view(), name="login"),
    path("register/", CustomUserRegistrationApiView.as_view(), name="register"),
    path("logout/", CustomUserLogoutApiView.as_view(), name="logout"),
    path("api-token-auth/", CustomAuthToken.as_view(), name="get-token"),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),

]