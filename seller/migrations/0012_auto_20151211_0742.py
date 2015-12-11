# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0011_auto_20151207_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='seller',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='products',
            name='age',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='video',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='timings',
            field=models.CharField(max_length=200),
        ),
    ]
