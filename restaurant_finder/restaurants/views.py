from django.shortcuts import render
from rest_framework import generics
from .models import Restaurant, MenuItem, Review
from .serializers import RestaurantSerializer, MenuItemSerializer, ReviewSerializer
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # Optional, safer default
from rest_framework.renderers import JSONRenderer
from .models import Restaurant

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows viewing without login, but requires auth for adding
    renderer_classes = [JSONRenderer]  # Ensures only JSON is rendered (no browsable API)
        

    def get_queryset(self):
        queryset = Restaurant.objects.all()
       
        # Filters
        cuisine = self.request.query_params.get('cuisine')
        max_price = self.request.query_params.get('max_price')
        
        if cuisine:
            queryset = queryset.filter(cuisine__iexact=cuisine)
        if max_price:
            queryset = queryset.filter(price_range__lte=max_price)
            
        return queryset
        
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

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


class RestaurantRecommendations(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    
    def get_queryset(self):
        cuisine = self.request.query_params.get('cuisine', None)
        min_rating = self.request.query_params.get('min_rating', 4.0)
        
        queryset = Restaurant.objects.annotate(
            avg_rating=Avg('reviews__rating')
        ).filter(avg_rating__gte=min_rating)
        
        if cuisine:
            queryset = queryset.filter(cuisine__iexact=cuisine)
            
        return queryset.order_by('-avg_rating')[:5]
    

def restaurant_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants.html', {'restaurants': restaurants})