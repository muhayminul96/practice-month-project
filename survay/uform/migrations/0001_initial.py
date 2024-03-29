# Generated by Django 3.1.7 on 2021-03-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
            ],
        ),
    ]
