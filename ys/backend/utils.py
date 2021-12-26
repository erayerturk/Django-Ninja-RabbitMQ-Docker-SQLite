import json
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django.db import utils

from backend.consumer import consume
from backend.enums import OrderStatus
from backend.models import Order, Food

scheduler = BackgroundScheduler(
    {"apscheduler.executors.default": {"class": "apscheduler.executors.pool:ThreadPoolExecutor", "max_workers": "1"},
     "apscheduler.executors.processpool": {"type": "processpool", "max_workers": "1"},
     "apscheduler.job_defaults.coalesce": "false", "apscheduler.job_defaults.max_instances": "3",
     "apscheduler.timezone": "UTC"})

logger = logging.getLogger(__name__)


@scheduler.scheduled_job('interval', seconds=10)
def get_order():
    def callback(ch, method, properties, body):
        data = json.loads(body)

        try:
            order = Order.objects.create(restaurant_id=data['restaurant'],
                                         deliver_to_id=data['deliver_to'],
                                         status=OrderStatus.WAITING.value)

            for food_id in data['foods']:
                order.foods.add(Food.objects.get(pk=food_id))

            order.save()
        except utils.IntegrityError:
            logger.warning(f"Restaurant or deliver owner is not exist >> {data}")
        except Food.DoesNotExist:
            order.delete()
            logger.warning(f"Food does not exist >> {data}")

    consume(callback)
