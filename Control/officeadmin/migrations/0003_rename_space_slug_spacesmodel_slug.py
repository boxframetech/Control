# Generated by Django 3.2 on 2021-07-06 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officeadmin', '0002_auto_20210706_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spacesmodel',
            old_name='space_slug',
            new_name='slug',
        ),
    ]