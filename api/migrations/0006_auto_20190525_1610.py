# Generated by Django 2.2.1 on 2019-05-25 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190525_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='createdBy',
            new_name='created_by',
        ),
    ]
