# Generated by Django 3.2 on 2021-07-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeadmin', '0007_rename_companyname_spaceusersmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='duration',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilitator',
            name='agreement_doc',
            field=models.FileField(blank=True, null=True, upload_to='facilitators/<django.db.models.fields.CharField>/'),
        ),
        migrations.AddField(
            model_name='facilitator',
            name='courses',
            field=models.ManyToManyField(to='officeadmin.CourseModel'),
        ),
        migrations.AddField(
            model_name='facilitator',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='facilitator',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentsmodel',
            name='courses',
            field=models.ManyToManyField(to='officeadmin.CourseModel'),
        ),
        migrations.AddField(
            model_name='studentsmodel',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='studentsmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentsmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
