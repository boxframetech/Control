# Generated by Django 3.2 on 2021-07-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeadmin', '0005_auto_20210706_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='spaceusersmodel',
            name='space_used',
            field=models.ManyToManyField(to='officeadmin.SpacesModel'),
        ),
    ]
