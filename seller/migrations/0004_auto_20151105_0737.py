# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_files_timings'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('reason', models.TextField()),
                ('listed', models.DateField()),
                ('sold', models.BooleanField()),
                ('video', models.TextField()),
                ('picture', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sellers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('picture', models.TextField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('size', models.IntegerField()),
                ('address', models.TextField()),
                ('desc', models.TextField()),
                ('video', models.TextField()),
                ('timings', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='files',
        ),
    ]
