from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase

from api import models


class TestPlanes(APITestCase):
    def setUp(self):
        self.fake = Faker()

    def test_successfully_create_plane(self):
        """
        Tests that user can create a plane entry when they supply `id` and
        `passenger` field values of type PositiveSmallInteger (0 - 32767).
        """
        # assert that database contains no Plane objects
        planes = models.Plane.objects.all()
        self.assertEqual(len(planes), 0)
        # create plane entry
        data = {
            'id': self.fake.random_int(max=32767),
            'passengers': self.fake.random_int(max=32767),
        }
        url = reverse('planes-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        # assert that database contains one Plane object
        planes = models.Plane.objects.all()
        self.assertEqual(len(planes), 1)
        plane = planes[0]
        self.assertEqual(plane.id, data['id'])
        self.assertEqual(plane.passengers, data['passengers'])