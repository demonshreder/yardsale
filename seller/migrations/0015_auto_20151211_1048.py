# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0014_auto_20151211_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='seller',
            field=models.ForeignKey(default=uuid.uuid4, to=settings.AUTH_USER_MODEL),
        ),
    ]
