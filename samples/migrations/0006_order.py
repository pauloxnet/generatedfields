from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samples", "0005_item"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("creation", models.DateTimeField()),
                ("payment", models.DateTimeField(null=True)),
                (
                    "status",
                    models.GeneratedField(
                        db_persist=True,
                        expression=models.Case(
                            models.When(
                                payment__isnull=False, then=models.Value("paid")
                            ),
                            default=models.Value("created"),
                        ),
                        output_field=models.TextField(),
                    ),
                ),
            ],
        ),
    ]
