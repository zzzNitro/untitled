# Generated by Django 3.0.4 on 2020-05-28 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_lesson_dlc_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dlc',
            name='course',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='dlc_files',
        ),
        migrations.AddField(
            model_name='dlc',
            name='lesson',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Lesson'),
        ),
    ]