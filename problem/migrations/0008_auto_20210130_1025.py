# Generated by Django 3.1.3 on 2021-01-30 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0007_auto_20210124_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submits', to='problem.problem'),
        ),
    ]
