# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_front', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cate',
            options={'verbose_name': '\u5206\u7c7b'},
        ),
        migrations.AddField(
            model_name='cate',
            name='media',
            field=models.FileField(help_text=b'\xe5\x88\x86\xe7\xb1\xbb\xe7\x9f\xad\xe7\x89\x87', null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='cate',
            name='query_code',
            field=models.CharField(help_text=b'\xe7\x94\xa8\xe4\xba\x8e\xe6\x9f\xa5\xe8\xaf\xa2\xe5\x88\x86\xe7\xb1\xbb\xe5\xae\x9e\xe4\xbe\x8b', max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cate',
            name='url',
            field=models.CharField(help_text=b'\xe5\x88\x86\xe7\xb1\xbb\xe7\x9a\x84url', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cate',
            name='description',
            field=models.CharField(help_text=b'\xe5\x88\x86\xe7\xb1\xbb\xe7\xae\x80\xe4\xbb\x8b', max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cate',
            name='parent',
            field=models.ForeignKey(related_name='children', verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe5\x88\x86\xe7\xb1\xbb', blank=True, to='pc_front.Cate', null=True),
        ),
    ]
