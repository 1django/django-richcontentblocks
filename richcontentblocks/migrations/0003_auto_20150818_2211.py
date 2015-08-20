# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('richcontentblocks', '0002_auto_20150818_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='create_date',
            new_name='created',
        ),
    ]
