# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-10 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(choices=[(0, '男'), (1, '女')])),
                ('clss', models.CharField(max_length=10)),
            ],
        ),
    ]
