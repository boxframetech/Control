# Generated by Django 3.2 on 2021-07-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_rename_weeklyprojections_weeklyprojection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalmodel',
            name='transaction_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
