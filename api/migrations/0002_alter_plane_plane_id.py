# Generated by Django 5.0 on 2023-12-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plane',
            name='plane_id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
    ]