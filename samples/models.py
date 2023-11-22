from django.db import models
from django.db.models import Case, F, Value, When
from django.db.models.functions import (
    Cos,
    Pi,
    Power,
    Radians,
    Round,
    Sin,
    TruncDate,
)


class Rectangle(models.Model):
    base = models.FloatField()
    height = models.FloatField()
    area = models.GeneratedField(
        expression=F("base") * F("height"),
        output_field=models.FloatField(),
        db_persist=True,
    )

    def __str__(self):
        return f"{self.base}×{self.height}={self.area}"


class Square(models.Model):
    side = models.FloatField()
    area = models.GeneratedField(
        expression=Power("side", 2),
        output_field=models.FloatField(),
        db_persist=True,
    )

    def __str__(self):
        return f"{self.side}²={self.area}"


class Circle(models.Model):
    radius = models.FloatField()
    area = models.GeneratedField(
        expression=Round(
            Power("radius", 2) * Pi(),
            precision=2,
        ),
        output_field=models.FloatField(),
        db_persist=True,
    )

    def __str__(self):
        return f"{self.radius}²×π={self.area}"


class RightTriangle(models.Model):
    hypotenuse = models.FloatField()
    angle = models.FloatField()
    area = models.GeneratedField(
        expression=Round(
            (Power("hypotenuse", 2) * Sin(Radians("angle")) * Cos(Radians("angle")))
            / 2,
            precision=2,
        ),
        output_field=models.FloatField(),
        db_persist=True,
    )

    def __str__(self):
        return f"{self.hypotenuse}²×sin({self.angle}°)×cos({self.angle}°)÷2={self.area}"


class Item(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(db_default=Value(1))
    total_price = models.GeneratedField(
        expression=F("price") * F("quantity"),
        output_field=models.DecimalField(max_digits=11, decimal_places=2),
        db_persist=True,
    )

    def __str__(self):
        return f"{self.price}×{self.quantity}={self.total_price}"


class Order(models.Model):
    creation = models.DateTimeField()
    payment = models.DateTimeField(null=True)
    status = models.GeneratedField(
        expression=Case(
            When(
                payment__isnull=False,
                then=Value("paid"),
            ),
            default=Value("created"),
        ),
        output_field=models.TextField(),
        db_persist=True,
    )

    def __str__(self):
        return f"[{self.status}] {self.payment or self.creation}"


class Event(models.Model):
    start = models.DateTimeField()
    start_date = models.GeneratedField(
        expression=TruncDate("start"),
        output_field=models.DateField(),
        db_persist=True,
    )
    end = models.DateTimeField(null=True)
    end_date = models.GeneratedField(
        expression=TruncDate("end"),
        output_field=models.DateField(),
        db_persist=True,
    )
    duration = models.GeneratedField(
        expression=F("end") - F("start"),
        output_field=models.DurationField(),
        db_persist=True,
    )

    def __str__(self):
        return f"[{self.duration or '∞'}] {self.start_date}…{self.end_date or ''}"


class Package(models.Model):
    slug = models.SlugField()
    data = models.JSONField()
    version = models.GeneratedField(
        expression=F("data__info__version"),
        output_field=models.TextField(),
        db_persist=True,
    )

    def __str__(self):
        return f"{self.slug} {self.version}"
