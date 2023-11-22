import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samples", "0008_package"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                (
                    "full_name",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.functions.text.Concat(
                            "first_name", models.Value(" "), "last_name"
                        ),
                        output_field=models.TextField(),
                    ),
                ),
            ],
        ),
    ]
