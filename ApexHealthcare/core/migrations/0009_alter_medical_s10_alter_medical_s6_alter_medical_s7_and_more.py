# Generated by Django 4.2.9 on 2024-05-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_medical_s10_medical_s6_medical_s7_medical_s8_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medical",
            name="s10",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="medical",
            name="s6",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="medical",
            name="s7",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="medical",
            name="s8",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="medical",
            name="s9",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
