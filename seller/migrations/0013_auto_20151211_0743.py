# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0012_auto_20151211_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='seller',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
