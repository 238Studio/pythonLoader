# myapp/tests.py
from django.test import TestCase
from django.urls import reverse
from django.db import models

class MyDjangoTests(TestCase):
    class Item(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()

        def __str__(self):
            return self.name

    def setUp(self):
        self.item = self.Item.objects.create(name='Test Item', description='This is a test item.')

    def test_item_str(self):
        self.assertEqual(str(self.item), 'Test Item')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Items')
        self.assertTemplateUsed(response, 'index.html')
