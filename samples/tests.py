from django.test import TestCase

from samples.models import (
    Circle,
    Event,
    Item,
    Order,
    Package,
    Rectangle,
    RightTriangle,
    Square,
)


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


class OrderTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.createdorder = Order.objects.create(creation="2023-01-01 12:00Z")
        cls.paidorder = Order.objects.create(
            creation="2023-01-02 00:00Z",
            payment="2023-01-03 06:30Z",
        )

    def test_str(self):
        self.assertEqual(str(self.createdorder), "[created] 2023-01-01 12:00Z")
        self.assertEqual(str(self.paidorder), "[paid] 2023-01-03 06:30Z")


class EventTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.startevent = Event.objects.create(start="2023-1-1 12:00Z")
        cls.endevent = Event.objects.create(
            start="2023-1-1 11:45Z", end="2023-1-9 00:00Z"
        )

    def test_str(self):
        self.assertEqual(str(self.startevent), "[∞] 2023-01-01…")
        self.assertEqual(str(self.endevent), "[7 days, 12:15:00] 2023-01-01…2023-01-09")


class PackageTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.package = Package.objects.create(
            slug="django", data={"info": {"version": "4.2.7"}}
        )

    def test_str(self):
        self.assertEqual(str(self.package), "django 4.2.7")
