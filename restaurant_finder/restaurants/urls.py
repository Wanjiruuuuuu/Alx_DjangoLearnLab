from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerList, RestaurantList, RestaurantDetail, MenuItemList, ReviewCreate, RestaurantRecommendations


urlpatterns = [
    path('all/', RestaurantList.as_view(), name='restaurant-list'),
    path('<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
    path('<int:restaurant_id>/menu/', MenuItemList.as_view(), name='menu-list'),
    path('<int:restaurant_id>/reviews/', ReviewCreate.as_view(), name='review-create'),
    path('customers/', CustomerList.as_view(), name='customers-create'),
    path('recommendations/', RestaurantRecommendations.as_view()),
] 