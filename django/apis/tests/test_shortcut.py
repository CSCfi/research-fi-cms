from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from contentapp.models import Shortcut
from contentapp.serializers import ShortcutSerializer

class ShortcutViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.shortcut = Shortcut.objects.create(
            placement_id = 1,
            lang = 'FI',
            link = 'https://research.fi',
            title_fi = 'Test Title FI',
            title_sv = 'Test Title SV',
            title_en = 'Test Title EN',
            content_fi = 'Test Content FI',
            content_sv = 'Test Content SV',
            content_en = 'Test Content EN',
            image = None,
            image_alt_fi = 'Test Image Alt FI',
            image_alt_sv = 'Test Image Alt SV',
            image_alt_en = 'Test Image Alt EN'
        )

    def test_get_shortcut_list(self):
        url = reverse('shortcut-list')
        response = self.client.get(url)
        shortcuts = Shortcut.objects.all()
        serializer = ShortcutSerializer(shortcuts, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
