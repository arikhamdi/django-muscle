# Generated by Django 3.1.4 on 2021-01-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0008_auto_20210105_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]