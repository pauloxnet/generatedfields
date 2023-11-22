from django.db import models
from django.db.models import F
from django.db.models.functions import (
    Pi,
    Power,
    Round,
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
