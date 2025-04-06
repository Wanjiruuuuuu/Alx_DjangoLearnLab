from django.contrib import admin
from .models import Restaurant, MenuItem, Customer, Review

admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Customer)
admin.site.register(Review)
