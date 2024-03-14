from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from contentapp.models import ExternalLinksParent
from contentapp.serializers import ExternalLinksParentSerializer

class ExternalLinkViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.external_link = ExternalLinksParent.objects.create(
            #parent=None,
            placement_id=2,
            #order_field_name='placement_id',
            #order_with_respect_to='parent',
            lang='FI',
            label_fi='Test Label FI',
            label_sv='Test Label SV',
            label_en='Test Label EN',
            content_fi='Test Content FI',
            content_sv='Test Content SV',
            content_en='Test Content EN',
            url_fi='https://research.fi/fi',
            url_sv='https://research.fi/sv',
            url_en='https://research.fi/en'
        )

    def test_get_all_external_links(self):
        url = reverse('externallink-list')
        response = self.client.get(url)
        external_links = ExternalLinksParent.objects.all()
        serializer = ExternalLinksParentSerializer(external_links, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_external_link(self):
        url = reverse('externallink-detail', args=[self.external_link.id])
        response = self.client.get(url)
        serializer = ExternalLinksParentSerializer(self.external_link)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)