# Generated by Django 3.1.3 on 2020-11-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('was_rest', '0003_auto_20201105_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]
