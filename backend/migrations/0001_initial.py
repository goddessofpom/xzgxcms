# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'\xe8\xbd\xae\xe6\x92\xad\xe5\x90\x8d\xe7\xa7\xb0', max_length=100)),
                ('query_code', models.CharField(help_text=b'\xe7\x94\xa8\xe4\xba\x8e\xe6\x9f\xa5\xe8\xaf\xa2\xe8\xbd\xae\xe6\x92\xad', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(help_text=b'\xe8\xbd\xae\xe6\x92\xad\xe5\x9b\xbe\xe7\x89\x87', upload_to=b'carousel_img')),
                ('title', models.CharField(help_text=b'\xe8\xbd\xae\xe6\x92\xad\xe6\xa0\x87\xe9\xa2\x98', max_length=200)),
                ('desc', models.CharField(help_text=b'\xe8\xbd\xae\xe6\x92\xad\xe7\xae\x80\xe4\xbb\x8b', max_length=200)),
                ('url', models.CharField(help_text=b'\xe8\xbd\xae\xe6\x92\xad\xe6\x89\x80\xe6\x8c\x87\xe5\x90\x91\xe7\x9a\x84url', max_length=500)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('carousel', models.ForeignKey(help_text=b'\xe6\x89\x80\xe5\xb1\x9e\xe8\xbd\xae\xe6\x92\xad', to='backend.Carousel')),
            ],
        ),
    ]
