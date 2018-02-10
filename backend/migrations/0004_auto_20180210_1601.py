# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20180202_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('index', models.IntegerField(default=0, help_text=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.AlterModelOptions(
            name='operationlog',
            options={'ordering': ['-created_time']},
        ),
    ]
