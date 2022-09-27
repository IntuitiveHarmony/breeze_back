# Generated by Django 4.1.1 on 2022-09-27 16:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeze_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequence',
            name='polyCsDelay',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='sequence',
            name='polyCsDist',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='sequence',
            name='polyCsFilter',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='sequence',
            name='polyCsReverb',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='sequence',
            name='polyCsSteps',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=10), null=True, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sequence',
            name='polyCsSynth',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='sequence',
            name='polyCsVolume',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='name',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='tempo',
            field=models.IntegerField(default=0),
        ),
    ]