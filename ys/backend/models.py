from django.db import models

from backend.enums import OrderStatus


class StarterModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(StarterModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)


class Restaurant(StarterModel):
    name = models.CharField(max_length=100)


class FoodCategory(StarterModel):
    name = models.CharField(max_length=100)


class Food(StarterModel):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    food_category = models.ForeignKey(FoodCategory, on_delete=models.PROTECT)


class Order(StarterModel):
    foods = models.ManyToManyField(Food)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    deliver_to = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    status = models.SmallIntegerField(default=OrderStatus.WAITING)
