from django.contrib import admin
from .models import Restaurant, FoodCategory, Food, CustomUser

admin.site.register(Restaurant)
admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(CustomUser)
