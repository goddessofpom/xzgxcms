# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_front', '0003_auto_20171210_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'article_img')),
                ('title', models.CharField(help_text=b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xa0\x87\xe9\xa2\x98', max_length=200, null=True, blank=True)),
                ('description', models.CharField(help_text=b'\xe5\x9b\xbe\xe7\x89\x87\xe7\xae\x80\xe4\xbb\x8b', max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='cate',
            name='is_article',
            field=models.BooleanField(default=0, help_text=b'\xe5\x88\x86\xe7\xb1\xbb\xe4\xb8\x8b\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x96\x87\xe7\xab\xa0\xef\xbc\x8c0\xef\xbc\x9a\xe6\x97\xa0\xef\xbc\x8c1\xef\xbc\x9a\xe6\x9c\x89'),
        ),
        migrations.AddField(
            model_name='imgarticle',
            name='display_mode',
            field=models.IntegerField(default=0, help_text=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x98\xbe\xe7\xa4\xba\xe6\xa8\xa1\xe5\xbc\x8f\xef\xbc\x8c0\xef\xbc\x9a\xe6\xa0\x87\xe5\x87\x86\xe6\xa8\xa1\xe5\xbc\x8f\xef\xbc\x8c1\xef\xbc\x9a\xe5\xa4\x9a\xe5\x9b\xbe\xe6\xa8\xa1\xe5\xbc\x8f'),
        ),
        migrations.AddField(
            model_name='imgarticle',
            name='label',
            field=models.CharField(help_text=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe7\xad\xbe', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='imgarticle',
            name='status',
            field=models.BooleanField(default=0, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xae\xa1\xe6\xa0\xb8\xef\xbc\x8c0\xef\xbc\x9a\xe6\x9c\xaa\xe5\xae\xa1\xe6\xa0\xb8\xef\xbc\x8c1\xef\xbc\x9a\xe5\xb7\xb2\xe5\xae\xa1\xe6\xa0\xb8'),
        ),
        migrations.AddField(
            model_name='images',
            name='article',
            field=models.ForeignKey(help_text=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x96\x87\xe7\xab\xa0', to='pc_front.ImgArticle'),
        ),
    ]
