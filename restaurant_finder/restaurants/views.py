from django.shortcuts import render
from rest_framework import generics
from .models import Restaurant, MenuItem, Review
from .serializers import RestaurantSerializer, MenuItemSerializer, ReviewSerializer

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuItemList(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    
    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return MenuItem.objects.filter(restaurant_id=restaurant_id)

class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        restaurant_id = self.kwargs['restaurant_id']
        restaurant = Restaurant.objects.get(id=restaurant_id)
        serializer.save(restaurant=restaurant)