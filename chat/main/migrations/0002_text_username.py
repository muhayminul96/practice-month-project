# Generated by Django 3.2.7 on 2021-09-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='username',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
