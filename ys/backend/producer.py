import os

import pika
from django.conf import settings

credentials = pika.PlainCredentials(settings.RABBITMQ_USER,
                                    settings.RABBITMQ_PASS)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.environ.get("RABBITMQ_HOST", "localhost"),
                              port=os.environ.get("RABBITMQ_PORT", 5672),
                              heartbeat=600,
                              blocked_connection_timeout=300,
                              credentials=credentials))
channel = connection.channel()


def publish(body):
    channel.basic_publish(exchange='', routing_key='orders', body=body)
