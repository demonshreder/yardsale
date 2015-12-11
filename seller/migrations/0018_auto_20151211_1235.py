# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0017_auto_20151211_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_boy',
            field=models.OneToOneField(default=uuid.uuid4, to=settings.AUTH_USER_MODEL),
        ),
    ]
