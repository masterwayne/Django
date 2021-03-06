# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_auto_20151227_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='joined',
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], default=b'M', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='ob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(default=b'0000000', max_length=8),
        ),
        migrations.AddField(
            model_name='user',
            name='street_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=b'budhu', max_length=50, unique=True),
        ),
    ]
