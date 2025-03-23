from django.core.management.base import BaseCommand
from restaurants.models import Restaurant, MenuItem, Customer, Review

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        # Create Restaurants
        restaurant1 = Restaurant.objects.create(
            name="Foodie Hub",
            location="Nairobi",
            cuisine="Italian",
            price_range="$$",
            rating=4.5
        )
        restaurant2 = Restaurant.objects.create(
            name="Spicy Bites",
            location="Mombasa",
            cuisine="Indian",
            price_range="$$$",
            rating=4.0
        )

        # Create Menu Items
        MenuItem.objects.create(
            restaurant=restaurant1,
            dish="Pasta Alfredo",
            price=700,
            description="Creamy Italian pasta"
        )
        MenuItem.objects.create(
            restaurant=restaurant1,
            dish="Tiramisu",
            price=300,
            description="Classic Italian dessert"
        )
        MenuItem.objects.create(
            restaurant=restaurant2,
            dish="Chicken Biryani",
            price=1000,
            description="Spiced rice & chicken"
        )

        # Create Customers
        customer1 = Customer.objects.create(
            username="rachel",
            email="rachel@example.com",
            password="password123"
        )
        customer2 = Customer.objects.create(
            username="alex",
            email="alex@example.com",
            password="password123"
        )

        # Create Reviews
        Review.objects.create(
            restaurant=restaurant1,
            customer=customer1,
            rating=5,
            comment="Amazing food and service!"
        )
        Review.objects.create(
            restaurant=restaurant2,
            customer=customer2,
            rating=4,
            comment="Great biryani but slow service."
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))