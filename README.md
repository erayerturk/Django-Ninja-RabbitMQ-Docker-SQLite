# Django Ninja - RabbitMQ - Docker - SQLite

Hello, there are six endpoints and one background task;

* */order/publish* endpoint send orders to RabbitMQ and no record to database
* *get_order* task consume the orders and record to database with "WAITING" status, this task also logging unsuccessful attempts
* */order/list* endpoint list the orders with their status 
* */order/complete/{order_id}* endpoint is recording to database with "COMPLETE" status

* */restaurants*, */foods* and */users* endpoints are listing relevant information

### Technologies and Tools
* Python 3.8
* Django 4.0
* Django Ninja Rest Framework
* RabbitMQ
* Pika
* SQLite
* APScheduler

### Run the app in Docker

Everything is containerized. So all you need is Docker installed, and then you can build and run:

```
docker-compose up -d --build
```

And your app will be up on the *port 8000*

### Test

```
docker exec -it ysbackend python manage.py test
```

### Swagger API Doc

API Documentation is also saved in the main directory as PDF.
http://localhost:8000/api/v1/docs

### RabbitMQ Dasboard
If you want to follow the metrics
http://localhost:15672/

*Username: admin*
*Password: admin*

### Django Admin Dashboard

http://localhost:8000/admin

*Username: admin*
*Password: admin*

### Notes

Order status is enum field
10 means status of "WAITING"
20 means status of "COMPLETED"