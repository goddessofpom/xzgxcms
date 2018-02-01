# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_front', '0004_auto_20180112_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98', max_length=200)),
                ('cover', models.ImageField(help_text=b'\xe6\x96\x87\xe7\xab\xa0\xe5\xb0\x81\xe9\x9d\xa2', upload_to=b'article_img')),
                ('author', models.CharField(help_text=b'\xe6\x96\x87\xe7\xab\xa0\xe4\xbd\x9c\xe8\x80\x85', max_length=50, null=True, blank=True)),
                ('media', models.FileField(upload_to=b'article_media')),
                ('description', models.CharField(help_text=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xae\x80\xe4\xbb\x8b', max_length=500, null=True, blank=True)),
                ('label', models.CharField(help_text=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe7\xad\xbe', max_length=100, null=True, blank=True)),
                ('status', models.BooleanField(default=0, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xae\xa1\xe6\xa0\xb8\xef\xbc\x8c0\xef\xbc\x9a\xe6\x9c\xaa\xe5\xae\xa1\xe6\xa0\xb8\xef\xbc\x8c1\xef\xbc\x9a\xe5\xb7\xb2\xe5\xae\xa1\xe6\xa0\xb8')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('cate', models.ForeignKey(help_text=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x88\x86\xe7\xb1\xbb', to='pc_front.Cate')),
            ],
            options={
                'ordering': ['-update_time'],
                'verbose_name': '\u5f71\u89c6\u6587\u7ae0',
            },
        ),
        migrations.AlterModelOptions(
            name='imgarticle',
            options={'ordering': ['-update_time'], 'verbose_name': '\u56fe\u7247\u6587\u7ae0'},
        ),
    ]
