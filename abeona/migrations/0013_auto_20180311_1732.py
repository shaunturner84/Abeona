# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-11 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abeona', '0012_auto_20180311_1625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewfeature',
            options={'ordering': ('feature__name',)},
        ),
    ]