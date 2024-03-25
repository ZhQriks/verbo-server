# Generated by Django 4.1.4 on 2024-03-25 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation', models.TextField()),
                ('mediaUrl', models.URLField()),
                ('transcript', models.TextField(blank=True, null=True)),
                ('isPhoto', models.BooleanField(default=False)),
                ('viewCount', models.IntegerField(default=0)),
            ],
        ),
    ]