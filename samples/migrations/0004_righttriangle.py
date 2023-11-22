import django.db.models.expressions
import django.db.models.functions.math
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samples", "0003_circle"),
    ]

    operations = [
        migrations.CreateModel(
            name="RightTriangle",
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
                ("hypotenuse", models.FloatField()),
                ("angle", models.FloatField()),
                (
                    "area",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.functions.math.Round(
                            django.db.models.expressions.CombinedExpression(
                                django.db.models.expressions.CombinedExpression(
                                    django.db.models.expressions.CombinedExpression(
                                        django.db.models.functions.math.Power(
                                            "hypotenuse", 2
                                        ),
                                        "*",
                                        django.db.models.functions.math.Sin(
                                            django.db.models.functions.math.Radians(
                                                "angle"
                                            )
                                        ),
                                    ),
                                    "*",
                                    django.db.models.functions.math.Cos(
                                        django.db.models.functions.math.Radians("angle")
                                    ),
                                ),
                                "/",
                                models.Value(2),
                            ),
                            precision=2,
                        ),
                        output_field=models.FloatField(),
                    ),
                ),
            ],
        ),
    ]
