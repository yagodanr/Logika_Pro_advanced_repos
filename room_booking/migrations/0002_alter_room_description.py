# Generated by Django 5.0.2 on 2024-02-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
