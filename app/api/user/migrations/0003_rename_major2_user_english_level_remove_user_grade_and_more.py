# Generated by Django 4.1.4 on 2024-03-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_user_group"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="major2",
            new_name="english_level",
        ),
        migrations.RemoveField(
            model_name="user",
            name="grade",
        ),
        migrations.RemoveField(
            model_name="user",
            name="grade_letter",
        ),
        migrations.RemoveField(
            model_name="user",
            name="group",
        ),
        migrations.RemoveField(
            model_name="user",
            name="major1",
        ),
        migrations.RemoveField(
            model_name="user",
            name="standard",
        ),
        migrations.AddField(
            model_name="user",
            name="balance",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="user",
            name="day_streak",
            field=models.IntegerField(default=0),
        ),
    ]
