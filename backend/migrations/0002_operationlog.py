# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('log_type', models.IntegerField(default=0, help_text=b'0:\xe5\x86\x85\xe5\xae\xb9\xe6\x97\xa5\xe5\xbf\x97\xef\xbc\x8c1\xef\xbc\x9a\xe7\xb3\xbb\xe7\xbb\x9f\xe6\x97\xa5\xe5\xbf\x97')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
