# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(unique=True, max_length=25)),
                ('password', models.CharField(max_length=100)),
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('date_joined', models.DateTimeField()),
            ],
        ),
    ]
