# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pc_front', '0008_city_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Famous',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('cover', models.ImageField(null=True, upload_to=b'article_img', blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='imgarticle',
            name='famous',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='pc_front.Famous', null=True),
        ),
    ]
