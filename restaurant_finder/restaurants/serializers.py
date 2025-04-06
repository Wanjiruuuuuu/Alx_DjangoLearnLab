from rest_framework import serializers
from .models import Restaurant, MenuItem, Review, Customer

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'dish', 'price', 'description']

class ReviewSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()  # Show customer username instead of ID
    class Meta:
        model = Review
        fields = ['id', 'customer', 'rating', 'comment']

class RestaurantSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'location', 'cuisine', 'price_range', 'rating', 'menu_items', 'reviews']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'password']