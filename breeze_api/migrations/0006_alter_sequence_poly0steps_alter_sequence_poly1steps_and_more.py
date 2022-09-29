# Generated by Django 4.1.1 on 2022-09-29 16:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeze_api', '0005_alter_sequence_poly0steps_alter_sequence_poly1steps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='poly0Steps',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=10), null=True, size=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sequence',
            name='poly1Steps',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=11), null=True, size=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sequence',
            name='poly2Steps',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=11), null=True, size=None),
            preserve_default=False,
        ),
    ]
