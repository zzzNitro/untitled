# Generated by Django 3.0.4 on 2020-05-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='dl_content',
            field=models.FileField(blank=True, null=True, upload_to='dlc/{course}/'),
        ),
    ]
