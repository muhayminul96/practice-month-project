# Generated by Django 3.1.7 on 2021-04-06 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210406_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='number',
            new_name='numberOfPeople',
        ),
    ]