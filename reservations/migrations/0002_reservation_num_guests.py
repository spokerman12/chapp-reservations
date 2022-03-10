# Generated by Django 3.2.12 on 2022-03-10 03:55

from django.db import migrations, models
import reservations.validators


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="num_guests",
            field=models.IntegerField(
                default=1, validators=[reservations.validators.validate_guests]
            ),
        ),
    ]
