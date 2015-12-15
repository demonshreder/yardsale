# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0019_auto_20151211_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(default='static/img/placeholder.jpg', upload_to='product_images'),
        ),
    ]
