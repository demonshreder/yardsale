# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0013_auto_20151211_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='seller',
            field=models.OneToOneField(default=uuid.uuid4, to=settings.AUTH_USER_MODEL),
        ),
    ]
