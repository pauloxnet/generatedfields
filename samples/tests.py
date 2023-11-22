from django.test import TestCase

from samples.models import Circle, Item, Rectangle, RightTriangle, Square


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


class RightTriangleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.righttriangle = RightTriangle.objects.create(hypotenuse=5, angle=45)

    def test_str(self):
        self.assertEqual(str(self.righttriangle), "5²×sin(45°)×cos(45°)÷2=6.25")


class ItemTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.single_item = Item.objects.create(price=9.99)
        cls.multiple_item = Item.objects.create(price=4.99, quantity=2)

    def test_str(self):
        self.assertEqual(str(self.single_item), "9.99×1=9.99")
        self.assertEqual(str(self.multiple_item), "4.99×2=9.98")
