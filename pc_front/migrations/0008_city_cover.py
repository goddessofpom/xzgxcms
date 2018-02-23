# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_front', '0007_auto_20180222_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'cate_cover', blank=True),
        ),
    ]
