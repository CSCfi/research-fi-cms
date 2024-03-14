from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from contentapp.models import ExternalLink, ExternalLinksParent
from contentapp.serializers import ExternalLinkSerializer, ExternalLinksParentSerializer

class ExternalLinkViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.external_link_parent = ExternalLinksParent.objects.create(
            placement_id = 1,
            lang = 'FI',
            title_fi = 'Test parent title FI',
            title_sv = 'Test parent title SV',
            title_en = 'Test parent title EN'
        )
        self.external_link = ExternalLink.objects.create(
            parent = self.external_link_parent,
            placement_id = 2,
            lang = 'FI',
            label_fi = 'Test Label FI',
            label_sv = 'Test Label SV',
            label_en = 'Test Label EN',
            content_fi = 'Test Content FI',
            content_sv = 'Test Content SV',
            content_en = 'Test Content EN',
            url_fi = 'https://research.fi/fi',
            url_sv = 'https://research.fi/sv',
            url_en = 'https://research.fi/en'
        )

    def test_get_all_external_links(self):
        url = reverse('external_links-list')
        response = self.client.get(url)
        external_links = ExternalLinksParent.objects.all()
        serializer = ExternalLinksParentSerializer(external_links, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
