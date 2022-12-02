# Generated by Django 4.1.2 on 2022-12-02 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Executive_Counsil",
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
                ("ec_name", models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="EC_Post",
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
                ("ec_post", models.CharField(max_length=264, unique=True)),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HM_FoundationApp.executive_counsil",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EC_Number",
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
                ("ec_number", models.CharField(max_length=264, unique=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HM_FoundationApp.ec_post",
                    ),
                ),
            ],
        ),
    ]