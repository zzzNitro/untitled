# Generated by Django 3.0.4 on 2020-05-25 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson_dl_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='DlContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dl_archive', models.FileField(blank=True, null=True, upload_to='dlc/{course}/')),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='dl_content',
        ),
        migrations.AddField(
            model_name='lesson',
            name='dl_content',
            field=models.ManyToManyField(blank=True, to='courses.DlContent'),
        ),
    ]
