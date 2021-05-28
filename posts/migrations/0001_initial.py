# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('votes', models.IntegerField()),
            ],
        ),
    ]
