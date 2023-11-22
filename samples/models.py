from django.db import models
from django.db.models import F


class Rectangle(models.Model):
    base = models.FloatField()
    height = models.FloatField()
    area = models.GeneratedField(
        expression=F("base") * F("height"),
        output_field=models.FloatField(),
        db_persist=True,
    )

    def __str__(self):
        return f"{self.base}×{self.height}=" f"{self.area}"
