# Generated by Django 3.1.4 on 2021-01-04 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
