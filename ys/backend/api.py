from typing import List

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from ninja import Router

from .enums import OrderStatus
from .models import Order, Food, Restaurant, CustomUser
from .producer import publish
from .schemas import OrderRequestSchema, OrderResponseSchema, SuccessMessage, ConflictMessage, \
    FoodResponseSchema, CustomUserResponseSchema, \
    RestaurantResponseSchema

router = Router()


@router.post('/order/publish', response={200: SuccessMessage})
def publish_order(request, payload: OrderRequestSchema):
    publish(payload.json())
    return 200, {"success": "Order is successfully creating..."}


@router.get('/order/complete/{order_id}', response={200: SuccessMessage, 409: ConflictMessage})
def complete_order(request, order_id: int):
    order = get_object_or_404(Order, pk=order_id)
    if order.status == OrderStatus.WAITING.value:
        order.status = OrderStatus.COMPLETED.value
        order.save()
        return 200, {"success": f"The order with ({order.id}) id has been completed"}
    else:
        return 409, {"conflict": f"The order with ({order.id}) id already completed"}


@router.get('/order/list', response={200: OrderResponseSchema})
def list_orders(request, per_page: int, page: int):
    paginator = Paginator(Order.objects.get_queryset().order_by('id'), per_page)
    orders: List[Order] = list(paginator.get_page(page).object_list)
    return 200, {"per_page": per_page, "page": page, "orders": orders}


@router.get('/restaurants', response={200: RestaurantResponseSchema})
def list_restaurants(request, per_page: int, page: int):
    paginator = Paginator(Restaurant.objects.get_queryset().order_by('id'), per_page)
    restaurants: List[Restaurant] = list(paginator.get_page(page).object_list)
    return 200, {"per_page": per_page, "page": page, "restaurants": restaurants}


@router.get('/users', response={200: CustomUserResponseSchema})
def list_users(request, per_page: int, page: int):
    paginator = Paginator(CustomUser.objects.get_queryset().order_by('id'), per_page)
    users: List[CustomUser] = list(paginator.get_page(page).object_list)
    return 200, {"per_page": per_page, "page": page, "users": users}


@router.get('/foods', response={200: FoodResponseSchema})
def list_foods(request, per_page: int, page: int):
    paginator = Paginator(Food.objects.get_queryset().order_by('id'), per_page)
    foods: List[Food] = list(paginator.get_page(page).object_list)
    return 200, {"per_page": per_page, "page": page, "foods": foods}
