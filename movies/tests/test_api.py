import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')
from django.urls import reverse
from rest_framework.test import APITestCase


class MovieApiTestCase_test(APITestCase):
    def test_get(self):
        url = reverse('movie-list')
        print(url)
        response = self.client.get(url)
        print(response)