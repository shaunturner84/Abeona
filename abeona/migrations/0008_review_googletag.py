# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-10 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abeona', '0007_review_textdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='googletag',
            field=models.CharField(default='Norwich, UK', max_length=200, verbose_name='Google Location'),
        ),
    ]
