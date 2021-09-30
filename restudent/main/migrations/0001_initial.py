# Generated by Django 3.1.7 on 2021-04-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField(max_length=40)),
                ('submitTime', models.DateTimeField(auto_now_add=True)),
                ('date', models.TextField(max_length=40)),
                ('time', models.TextField(max_length=40)),
                ('number', models.IntegerField()),
                ('message', models.TextField(max_length=800)),
            ],
        ),
    ]
