# Generated by Django 4.1.2 on 2023-01-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HM_FoundationApp", "0006_add_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="add_image",
            name="images",
            field=models.ImageField(upload_to="images/"),
        ),
    ]