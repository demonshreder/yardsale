# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0010_remove_sellers_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('picture', models.URLField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('address', models.TextField(blank=True)),
                ('desc', models.TextField()),
                ('video', models.URLField(blank=True)),
                ('timings', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='sellers',
        ),
    ]
