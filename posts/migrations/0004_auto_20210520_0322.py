# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
