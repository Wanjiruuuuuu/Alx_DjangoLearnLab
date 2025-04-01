from django.urls import path
from .views import RestaurantList, RestaurantDetail, MenuItemList, ReviewCreate, RestaurantRecommendations

urlpatterns = [
    path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
    path('restaurants/<int:restaurant_id>/menu/', MenuItemList.as_view(), name='menu-list'),
    path('restaurants/<int:restaurant_id>/reviews/', ReviewCreate.as_view(), name='review-create'),
    path('api/recommendations/', RestaurantRecommendations.as_view()),
]