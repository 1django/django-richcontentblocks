# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('key', models.SlugField(help_text=b'The key used to access the content block in a template.  The system will generate this for you.', unique=True, blank=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('content_group', models.CharField(help_text=b'Group this content item belongs to.', max_length=50, blank=True)),
                ('content_type', models.CharField(default=b'CB', max_length=2, choices=[(b'CB', b'Content Block'), (b'PG', b'Page')])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Content Block',
            },
        ),
    ]
