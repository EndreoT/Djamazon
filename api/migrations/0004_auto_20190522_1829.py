# Generated by Django 2.2.1 on 2019-05-23 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_department_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]