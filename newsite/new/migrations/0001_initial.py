# Generated by Django 2.2.2 on 2019-06-19 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField(max_length=300)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
