# Generated by Django 3.1.3 on 2021-05-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('course', '0003_delete_courseprogress'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseschedule',
            name='lessons',
            field=models.JSONField(default='{}', null=True),
        ),
    ]