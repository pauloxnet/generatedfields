import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name="Rectangle",
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
                ("base", models.FloatField()),
                ("height", models.FloatField()),
                (
                    "area",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.expressions.CombinedExpression(
                            models.F("base"), "*", models.F("height")
                        ),
                        output_field=models.FloatField(),
                    ),
                ),
            ],
        ),
    ]
