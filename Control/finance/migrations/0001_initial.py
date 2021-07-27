# Generated by Django 3.2 on 2021-07-08 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('business_type', models.CharField(choices=[('Catering', 'Catering'), ('Plumber', 'Plumber'), ('Electrician', 'Electrician')], max_length=120)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DebtorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('service_rendered', models.CharField(blank=True, max_length=120, null=True)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JournalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('cr_account', models.CharField(blank=True, choices=[('Momo', 'Momo'), ('Bank', 'Bank'), ('Cash at Hand', 'Cash at Hand')], help_text='Where is the money leaving', max_length=120)),
                ('dr_account', models.CharField(blank=True, choices=[('Momo', 'Momo'), ('Bank', 'Bank'), ('Cash at Hand', 'Cash at Hand')], help_text='Where is the money going', max_length=120)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='what is money used for', null=True)),
                ('docs', models.FileField(blank=True, null=True, upload_to='finance/')),
                ('is_payable', models.BooleanField(default=False, help_text='if transaction is unpaid but has happen')),
                ('is_receivable', models.BooleanField(default=False, help_text='if transaction has happen but cash isnt received')),
                ('bank_activity', models.BooleanField(default=False, help_text='if the transaction pass through bank')),
                ('is_taxwitheld', models.BooleanField(default=False, help_text='if its a tax related')),
            ],
        ),
        migrations.CreateModel(
            name='PettycashModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_date', models.DateField()),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyProjections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('department', models.CharField(blank=True, max_length=120)),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PettyCashTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=2)),
                ('received_by', models.CharField(blank=True, max_length=120, null=True)),
                ('doc', models.FileField(upload_to='finance/pettycash/')),
                ('pettycash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.pettycashmodel')),
            ],
        ),
    ]