from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from contentapp.models import Page
from contentapp.serializers import PageSerializer

class PageViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.page = Page.objects.create(
            lang='FI',
            title_fi='Test Page FI',
            title_en='Test Page EN',
            title_sv='Test Page SV',
            content_fi='This is a test page FI.',
            content_en='This is a test page EN.',
            content_sv='This is a test page SV.',
            page_id='test_page'
        )

    def test_get_all_pages(self):
        url = reverse('page-list')
        response = self.client.get(url)
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_page(self):
        url = reverse('page-detail', args=[self.page.id])
        response = self.client.get(url)
        serializer = PageSerializer(self.page)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
