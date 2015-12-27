# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics/')),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='M')),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, help_text='Only Indian', unique=True, null=True)),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(max_length=8, default='0000000')),
                ('following', models.ManyToManyField(to='Accounts.MyUser', related_name='followers')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
