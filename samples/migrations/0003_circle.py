import django.db.models.expressions
import django.db.models.functions.math
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samples", "0002_square"),
    ]

    operations = [
        migrations.CreateModel(
            name="Circle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("radius", models.FloatField()),
                (
                    "area",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.functions.math.Round(
                            django.db.models.expressions.CombinedExpression(
                                django.db.models.functions.math.Power("radius", 2),
                                "*",
                                django.db.models.functions.math.Pi(),
                            ),
                            precision=2,
                        ),
                        output_field=models.FloatField(),
                    ),
                ),
            ],
        ),
    ]
