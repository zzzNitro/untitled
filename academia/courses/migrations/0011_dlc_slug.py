# Generated by Django 3.0.4 on 2020-05-28 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20200527_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='dlc',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]