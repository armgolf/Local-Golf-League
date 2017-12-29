# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0002_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='datetime',
        ),
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(default='none', max_length=234),
        ),
        migrations.AddField(
            model_name='payment',
            name='year',
            field=models.CharField(default='2017', max_length=4),
        ),
    ]