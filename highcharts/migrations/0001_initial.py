# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 10, 28, 0, 488115))),
                ('last_update', models.DateTimeField()),
                ('num_visits', models.SmallIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
