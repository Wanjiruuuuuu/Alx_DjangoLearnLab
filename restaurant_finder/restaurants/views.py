from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Restaurant, MenuItem, Review
from .serializers import RestaurantSerializer, MenuItemSerializer, ReviewSerializer, CustomerSerializer
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly # Optional, safer default
from rest_framework.renderers import JSONRenderer
from .models import Restaurant, Customer


class RestaurantList(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows viewing without login, but requires auth for adding
    # renderer_classes = [JSONRenderer]  # Ensures only JSON is rendered (no browsable API)
        

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
        
    # def get(self, request):
    #     restaurants = Restaurant.objects.all()
    #     serializer = RestaurantSerializer(restaurants, many=True)
    #     return Response(serializer.data)

class RestaurantDetail(APIView):
    # queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows viewing without login, but requires auth
    
    # Get ID from route and return it
    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response(status=404)

        return Response(RestaurantSerializer(restaurant).data)


class MenuItemList(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return MenuItem.objects.filter(restaurant_id=restaurant_id)

class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    def perform_create(self, serializer):
        restaurant_id = self.kwargs['restaurant_id']
        restaurant = Restaurant.objects.get(id=restaurant_id)
        serializer.save(restaurant=restaurant, customer=self.request.user)


class RestaurantRecommendations(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    def get_queryset(self):
        cuisine = self.request.query_params.get('cuisine', None)
        min_rating = self.request.query_params.get('min_rating', 4.0)
        
        queryset = Restaurant.objects.annotate(
            avg_rating=Avg('reviews__rating')
        ).filter(avg_rating__gte=min_rating)
        
        if cuisine:
            queryset = queryset.filter(cuisine__iexact=cuisine)
            
        return queryset.order_by('-avg_rating')[:5]

# Views To CRUD customers from the Customers model
class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Customer.objects.filter(username=self.request.user.username)
    
    def perform_create(self, serializer):
        serializer.save(username=self.request.user.username)

# def restaurant_page(request):
#     restaurants = Restaurant.objects.all()
#     return render(request, 'restaurants.html', {'restaurants': restaurants})

# def restaurant_page(request):
#     cuisine = request.GET.get('cuisine')
#     max_price = request.GET.get('max_price')

#     restaurants = Restaurant.objects.all()

#     if cuisine:
#         restaurants = restaurants.filter(cuisine__icontains=cuisine)
#     if max_price:
#         restaurants = restaurants.filter(price_range__lte=max_price)

#     return render(request, 'restaurants.html', {'restaurants': restaurants})
