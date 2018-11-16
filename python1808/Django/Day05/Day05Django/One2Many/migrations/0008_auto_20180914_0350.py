# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-14 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('One2Many', '0007_auto_20180914_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='One2Many.UserType'),
        ),
    ]