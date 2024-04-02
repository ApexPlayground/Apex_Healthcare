# Generated by Django 4.2.9 on 2024-04-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_profile_medical_appointment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="medical", old_name="symptom1", new_name="s1",
        ),
        migrations.RenameField(
            model_name="medical", old_name="symptom2", new_name="s2",
        ),
        migrations.RenameField(
            model_name="medical", old_name="symptom3", new_name="s3",
        ),
        migrations.RenameField(
            model_name="medical", old_name="symptom4", new_name="s4",
        ),
        migrations.RenameField(
            model_name="medical", old_name="symptom5", new_name="s5",
        ),
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                blank=True, default="profile/avatar.png", upload_to=""
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="country",
            field=models.CharField(default="Ireland", max_length=255),
        ),
    ]