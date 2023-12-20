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

    def test_cannot_create_plane_entry_without_id_field(self):
        """
        Tests that a plane entry cannot be made without required field `id`.
        """
        # assert that database contains no Plane objects
        planes = models.Plane.objects.all()
        self.assertEqual(len(planes), 0)
        # attempt to create plane entry
        data = {
            'passengers': self.fake.random_int(max=32767),
        }
        url = reverse('planes-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
        decoded = response.content.decode('utf-8')
        self.assertIn('This field is required', decoded)
        # assert that no plane entry was made in the database
        planes = models.Plane.objects.all()
        self.assertEqual(len(planes), 0)

    def test_cannot_create_plane_entry_without_passengers_field(self):
        """
        Tests that a plane entry cannot be made without required field
        `passengers`.
        """
        # assert that database contains no Plane objects
        planes = models.Plane.objects.all()
        self.assertEqual(len(planes), 0)
        # attempt to create plane entry
        data = {
            'id': self.fake.random_int(max=32767),
        }
        url = reverse('planes-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
        decoded = response.content.decode('utf-8')
        self.assertIn('This field is required', decoded)
        # assert that no plane entry was made in the database
        planes = models.Plane.objects.all()
        self.assertEqual(len(planes), 0)

    def test_cannot_create_plane_entry_without_id_and_passengers_field(self):
        """
        Tests that a plane entry cannot be made without both required fields
        `id` and `passengers`.
        """
        # assert that database contains no Plane objects
        planes = models.Plane.objects.all()
        self.assertEqual(len(planes), 0)
        # attempt to create plane entry
        data = {
            'random_field_1': self.fake.random_int(max=32767),
            'random_field_2': self.fake.random_int(max=32767),
        }
        url = reverse('planes-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
        json_response = response.json()
        id_error = json_response['id'][0]
        passenger_error = json_response['passengers'][0]
        self.assertIn('This field is required', id_error)
        self.assertIn('This field is required', passenger_error)
        # assert that no plane entry was made in the database
        planes = models.Plane.objects.all()
        self.assertEqual(len(planes), 0)