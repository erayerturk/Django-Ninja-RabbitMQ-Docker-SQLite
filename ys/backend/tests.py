import json

from django.test import TestCase


class APITest(TestCase):
    def setUp(self):
        self.content_type = "application/json"
        self.url = "http://localhost:8000/api/v1"
        self.order_id = 1

    def test_publish_order(self):
        payload = {
            "restaurant_with_diff_key": 1,
            "deliver_to": 1,
            "foods": [
                1
            ]
        }
        response = self.client.post(self.url + "/order/publish", data=json.dumps(payload),
                                    content_type=self.content_type)
        assert response.status_code == 422
        payload.pop("restaurant_with_diff_key")
        payload['restaurant'] = 1
        response = self.client.post(self.url + "/order/publish", data=json.dumps(payload),
                                    content_type=self.content_type)
        assert response.status_code == 200

    def test_complete_order(self):
        response = self.client.get(self.url + "/order/complete/99999999", content_type=self.content_type)
        assert response.status_code == 404

    def test_list(self):
        response = self.client.get(self.url + "/order/list?per_page=2&page=2", content_type=self.content_type)
        assert response.status_code == 200

    def test_list_restaurants(self):
        response = self.client.get(self.url + "/restaurants?per_page=2&page=2", content_type=self.content_type)
        assert response.status_code == 200

    def test_list_users(self):
        response = self.client.get(self.url + "/users?per_page=2&page=2", content_type=self.content_type)
        assert response.status_code == 200

    def test_list_foods(self):
        response = self.client.get(self.url + "/foods?per_page=2&page=2", content_type=self.content_type)
        assert response.status_code == 200
