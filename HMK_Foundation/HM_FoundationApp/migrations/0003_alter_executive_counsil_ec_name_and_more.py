# Generated by Django 4.1.2 on 2022-12-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "HM_FoundationApp",
            "0002_remove_ec_post_name_executive_counsil_ec_number_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="executive_counsil",
            name="ec_name",
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name="executive_counsil",
            name="ec_number",
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name="executive_counsil",
            name="ec_post",
            field=models.CharField(max_length=264, null=True),
        ),
    ]