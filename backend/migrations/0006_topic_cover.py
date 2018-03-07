# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_topic_topicarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'carousel_img', blank=True),
        ),
    ]
