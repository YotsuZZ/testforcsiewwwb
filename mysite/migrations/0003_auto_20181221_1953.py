# Generated by Django 2.1.3 on 2018-12-21 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20181221_1936'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category1',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category1',
            new_name='category',
        ),
    ]