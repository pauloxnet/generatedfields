from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samples", "0007_event"),
    ]

    operations = [
        migrations.CreateModel(
            name="Package",
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
                ("slug", models.SlugField()),
                ("data", models.JSONField()),
                (
                    "version",
                    models.GeneratedField(
                        db_persist=True,
                        expression=models.F("data__info__version"),
                        output_field=models.TextField(),
                    ),
                ),
            ],
        ),
    ]
