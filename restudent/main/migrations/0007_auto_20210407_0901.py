# Generated by Django 3.1.7 on 2021-04-07 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('starters', 'Starters'), ('salads', 'Salads'), ('specialty', 'Specialty')], max_length=100),
        ),
    ]
