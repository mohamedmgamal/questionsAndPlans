# Generated by Django 3.1.7 on 2022-01-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApi', '0004_auto_20220107_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='other',
            field=models.TextField(blank=True, null=True),
        ),
    ]