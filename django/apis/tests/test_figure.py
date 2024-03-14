from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from contentapp.models import Figure
from contentapp.serializers import FigureSerializer

class FigureViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.figure = Figure.objects.create(
            placement_id = 1,
            lang = 'FI',
            title_fi = 'Test title FI',
            title_sv = 'Test title SV',
            title_en = 'Test title EN'
        )

    def test_get_all_figures(self):
        url = reverse('figure-list')
        response = self.client.get(url)
        figures = Figure.objects.all()
        serializer = FigureSerializer(figures, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_figure(self):
        url = reverse('figure-detail', args=[self.figure.id])
        response = self.client.get(url)
        serializer = FigureSerializer(self.figure)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)