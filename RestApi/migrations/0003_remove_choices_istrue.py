# Generated by Django 3.1.7 on 2022-01-07 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestApi', '0002_answers_attemptid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choices',
            name='isTrue',
        ),
    ]
