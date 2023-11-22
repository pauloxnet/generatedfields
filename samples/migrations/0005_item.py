import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samples", "0004_righttriangle"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "quantity",
                    models.PositiveSmallIntegerField(db_default=models.Value(1)),
                ),
                (
                    "total_price",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.expressions.CombinedExpression(
                            models.F("price"), "*", models.F("quantity")
                        ),
                        output_field=models.DecimalField(
                            decimal_places=2, max_digits=11
                        ),
                    ),
                ),
            ],
        ),
    ]
