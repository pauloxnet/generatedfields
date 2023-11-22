import django.db.models.expressions
import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samples", "0006_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("start", models.DateTimeField()),
                (
                    "start_date",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.functions.datetime.TruncDate(
                            "start"
                        ),
                        output_field=models.DateField(),
                    ),
                ),
                ("end", models.DateTimeField(null=True)),
                (
                    "end_date",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.functions.datetime.TruncDate("end"),
                        output_field=models.DateField(),
                    ),
                ),
                (
                    "duration",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.expressions.CombinedExpression(
                            models.F("end"), "-", models.F("start")
                        ),
                        output_field=models.DurationField(),
                    ),
                ),
            ],
        ),
    ]
