# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('seller_id', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('picture', models.TextField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('size', models.IntegerField()),
                ('address', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
