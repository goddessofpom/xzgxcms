# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_operationlog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carouselitem',
            options={'permissions': (('add_carousel_item', '\u6dfb\u52a0\u8f6e\u64ad'), ('modify_carousel_item', '\u4fee\u6539\u8f6e\u64ad'), ('delete_carousel_item', '\u5220\u9664\u8f6e\u64ad'))},
        ),
    ]
