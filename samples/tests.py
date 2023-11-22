from django.test import TestCase

from samples.models import Rectangle


class RectangleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.rectangle = Rectangle.objects.create(base=6, height=7)

    def test_str(self):
        self.assertEqual(str(self.rectangle), "6×7=42.0")
