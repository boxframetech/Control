from django.db import models
from django.db.models.signals import pre_save
from Control.utils import unique_slug_generator

# Create your models here.
class CreditorModel(models.Model):
    ''' People iSpace owe'''
    businessType = (
        ("Catering","Catering"),
        ("Plumber","Plumber"),
        ("Electrician","Electrician"),
    )
    name = models.CharField(max_length=120, blank=True, null=True, help_text="People who iSpace work")
    slug = models.SlugField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    business_type = models.CharField(max_length=120,choices=businessType)
    location = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.slug

def creditor_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(creditor_pre_save_receiver, sender=CreditorModel)




class DebtorModel(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    service_rendered = models.CharField(max_length=120, blank=True,null=True)
    location = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.slug

def debtor_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(debtor_pre_save_receiver, sender=DebtorModel)



class JournalModel(models.Model):
    creditaccount = (
        ("Revenue","Revenue"),
        ("Momo","Momo"),
        ("Bank","Bank"),
        ("Cash at Hand","Cash at Hand"),
    )

    debitaccounts = (
        ("Momo","Momo"),
        ("Bank","Bank"),
        ("Cash at Hand","Cash at Hand"),
        ('Office Expense','Office Expense'),
        ('Statutory obligation','Statutory obligation'),
        ('Office Expense','Office Expense'),
        ('Office Expense','Office Expense'),
        ('Office Expense','Office Expense'),
    )

    transaction_date = models.DateTimeField(auto_now_add=True)
    cr_account = models.CharField(choices=creditaccount,max_length=120, blank=True, help_text='Where is the money leaving')
    dr_account = models.CharField(choices=debitaccounts,max_length=120, blank=True, help_text='Where is the money going')
    name = models.CharField(max_length=120, blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(help_text='what is money used for', blank=True, null=True)
    docs = models.FileField(upload_to='finance/journal', blank=True, null=True)
    is_payable = models.BooleanField(default=False, help_text='if transaction is unpaid but has happen')
    is_receivable = models.BooleanField(default=False, help_text='if transaction has happen but cash isnt received')
    bank_activity = models.BooleanField(default=False, help_text='if the transaction pass through bank')
    is_taxwitheld  =models.BooleanField(default=False, help_text='if its a tax related')

    def __str__(self):
        return self.slug

def journal_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(journal_pre_save_receiver, sender=JournalModel)



class PettycashModel(models.Model):
    received_date = models.DateField(auto_now_add=False)
    name = models.CharField(max_length=120, blank=True, null= True)
    slug = models.SlugField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.slug

def pettycash_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pettycash_pre_save_receiver, sender=PettycashModel)


class PettyCashTransaction(models.Model):
    pettycash = models.ForeignKey(PettycashModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    received_by = models.CharField(max_length=120, blank=True, null=True)
    doc = models.FileField(upload_to='finance/pettycash/', blank=True, null=True)

    def __str__(self):
        return self.slug

def pettycashtransaction_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pettycashtransaction_pre_save_receiver, sender=PettyCashTransaction)



class WeeklyProjection(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    department = models.CharField(max_length=120, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.description

