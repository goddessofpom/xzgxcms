# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0', max_length=200, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('cover', models.ImageField(help_text=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x9b\xbe\xe7\x89\x87', upload_to=b'cate_cover', verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x9b\xbe\xe7\x89\x87')),
                ('description', models.CharField(help_text=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\x8f\x8f\xe8\xbf\xb0', max_length=500, null=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe7\xae\x80\xe4\xbb\x8b', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='pc_front.Cate', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
