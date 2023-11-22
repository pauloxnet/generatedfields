from django.test import TestCase

from samples.models import Circle, Rectangle, Square


class RectangleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.rectangle = Rectangle.objects.create(base=6, height=7)

    def test_str(self):
        self.assertEqual(str(self.rectangle), "6×7=42.0")


class SquareTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.square = Square.objects.create(side=3)

    def test_str(self):
        self.assertEqual(str(self.square), "3²=9.0")


class CircleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.circle = Circle.objects.create(radius=3.1415)

    def test_str(self):
        self.assertEqual(str(self.circle), "3.1415²×π=31.0")
