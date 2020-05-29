# Generated by Django 3.0.4 on 2020-05-29 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20200529_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='dlc/'),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=75, null=True)),
                ('position', models.IntegerField()),
                ('files', models.FileField(upload_to='dlc/')),
                ('lesson', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson')),
            ],
        ),
    ]