# Generated by Django 3.2.15 on 2022-10-20 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_auto_20211230_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseprogress',
            name='attendance',
        ),
        migrations.AlterField(
            model_name='lessonprogress',
            name='attendance',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]