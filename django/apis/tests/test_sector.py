from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from contentapp.models import Sector
from contentapp.serializers import SectorSerializer

class SectorViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sector = Sector.objects.create(
            placement_id = 1,
            lang = 'FI',
            name_fi = 'Test Sector FI',
            name_sv = 'Test Sector SV',
            name_en = 'Test Sector EN',
            subtitle_fi = 'Test Subtitle FI',
            subtitle_sv = 'Test Subtitle SV',
            subtitle_en = 'Test Subtitle EN',
            iframe_fi = 'test_iframe_fi',
            iframe_sv = 'test_iframe_sv',
            iframe_en = 'test_iframe_en',
            description_fi = 'Test Description FI',
            description_sv = 'Test Description SV',
            description_en = 'Test Description EN',
            icon = 'Test Icon'
        )

    def test_get_all_sectors(self):
        url = reverse('sector-list')
        response = self.client.get(url)
        sectors = Sector.objects.all()
        serializer = SectorSerializer(sectors, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_sector(self):
        url = reverse('sector-detail', args=[self.sector.id])
        response = self.client.get(url)
        serializer = SectorSerializer(self.sector)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)