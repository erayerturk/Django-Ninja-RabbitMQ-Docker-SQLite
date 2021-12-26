from typing import List, Dict, Any

from ninja import Schema
from ninja.orm import create_schema

from backend.models import Order, Restaurant, FoodCategory, CustomUser, Food

# OrgOrderSchema = create_schema(Order, exclude=["created_at", "updated_at", "id"], depth=2)
excludes = ["created_at", "updated_at"]
RestaurantSchema = create_schema(Restaurant, exclude=excludes)
FoodCategorySchema = create_schema(FoodCategory, exclude=excludes)
# FoodSchema = create_schema(Food)
CustomUserSchema = create_schema(CustomUser, exclude=excludes)


class FoodSchema(Schema):
    name: str
    price: float
    description: str
    restaurant: RestaurantSchema
    food_category: FoodCategorySchema


class OrderSchema(Schema):
    id: int
    restaurant: RestaurantSchema
    deliver_to: CustomUserSchema
    foods: List[FoodSchema]
    status: int


class OrderRequestSchema(Schema):
    restaurant: int
    deliver_to: int
    foods: List[int]


class OrderResponseSchema(Schema):
    per_page: int
    page: int
    orders: List[OrderSchema]


class RestaurantResponseSchema(Schema):
    per_page: int
    page: int
    restaurants: List[RestaurantSchema]


class FoodResponseSchema(Schema):
    per_page: int
    page: int
    foods: List[FoodSchema]


class CustomUserResponseSchema(Schema):
    per_page: int
    page: int
    users: List[CustomUserSchema]


class ErrorMessage(Schema):
    errors: Dict[str, Any]


class SuccessMessage(Schema):
    success: str


class ConflictMessage(Schema):
    conflict: str
