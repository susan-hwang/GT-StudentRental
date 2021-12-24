# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gtrent', '0002_auto_20160409_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='Type',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='drivingTime',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='transitTime',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='walkingTime',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='BasePrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='Bathroom',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='Bedroom',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='Place_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gtrent.Property'),
        ),
        migrations.AlterField(
            model_name='price',
            name='TopPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Altitude',
            field=models.FloatField(default=33.0),
        ),
        migrations.AlterField(
            model_name='property',
            name='City',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Crime_Grade',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Estate_Name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Grade',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Longtitude',
            field=models.FloatField(default=33.0),
        ),
        migrations.AlterField(
            model_name='property',
            name='Phone_Number',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Place_ID',
            field=models.CharField(default='001', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='Website',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Yelp_Grade',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Zipcode',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='yelp',
            name='Place_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gtrent.Property'),
        ),
        migrations.AlterField(
            model_name='yelp_details',
            name='Address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='yelp_details',
            name='Category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='yelp_details',
            name='Name',
            field=models.CharField(default='111', max_length=100, primary_key=True, serialize=False),
        ),
    ]
