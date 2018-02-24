# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_front', '0005_auto_20180201_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imgarticle',
            options={'ordering': ['-update_time'], 'verbose_name': '\u56fe\u7247\u6587\u7ae0', 'permissions': (('add_img_article', '\u6dfb\u52a0\u56fe\u7247\u6587\u7ae0'), ('modify_img_article', '\u4fee\u6539\u56fe\u7247\u6587\u7ae0'), ('delete_img_article', '\u5220\u9664\u56fe\u7247\u6587\u7ae0'), ('confirm_img_article', '\u5ba1\u6838\u56fe\u7247\u6587\u7ae0'))},
        ),
        migrations.AlterModelOptions(
            name='mediaarticle',
            options={'ordering': ['-update_time'], 'verbose_name': '\u5f71\u89c6\u6587\u7ae0', 'permissions': (('add_media_article', '\u6dfb\u52a0\u89c6\u9891\u6587\u7ae0'), ('modify_media_article', '\u4fee\u6539\u89c6\u9891\u6587\u7ae0'), ('delete_media_article', '\u5220\u9664\u89c6\u9891\u6587\u7ae0'), ('confirm_media_article', '\u5ba1\u6838\u89c6\u9891\u6587\u7ae0'))},
        ),
    ]
