# Generated by Django 2.1.2 on 2018-10-16 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='Tweet_id_str',
        ),
    ]
