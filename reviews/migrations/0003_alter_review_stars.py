# Generated by Django 4.2.13 on 2024-08-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_alter_review_stars"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(
                choices=[
                    (0, "None"),
                    (1, "Poor"),
                    (2, "Ok"),
                    (3, "Average"),
                    (4, "Good"),
                    (5, "Excellent"),
                ],
                default="0",
            ),
        ),
    ]
