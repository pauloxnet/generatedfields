import django.db.models.functions.math
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samples", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Square",
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
                ("side", models.FloatField()),
                (
                    "area",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.functions.math.Power("side", 2),
                        output_field=models.FloatField(),
                    ),
                ),
            ],
        ),
    ]
