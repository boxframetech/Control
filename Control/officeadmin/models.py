from django.db import models
from django.db.models.signals import pre_save
from Control.utils import unique_slug_generator


# Create your models here.
class SpacesModel(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    space_img = models.ImageField(upload_to='spaces/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=9, blank=True, null=True, decimal_places=2)
    is_bookable = models.BooleanField(
        default=False, help_text='Only Tick is a space is bookable like event / meeting ')

    def __str__(self):
        return self.slug


def space_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(space_pre_save_receiver, sender=SpacesModel)


class SpaceusersModel(models.Model):
    space_used = models.ManyToManyField(SpacesModel)
    name = models.CharField(max_length=120, blank=True,
                            null=True, default='Company_name/name')
    slug = models.SlugField(blank=True, null=True)
    email = models.EmailField(unique=True, default='me@email.com', blank=True)
    phone = models.CharField(max_length=120, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.slug


def spaceuser_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(spaceuser_pre_save_receiver, sender=SpaceusersModel)


class SpaceUserPayment(models.Model):
    spaceuser = models.ForeignKey(SpaceusersModel, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120, blank=True,null=True)
    slug = models.SlugField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=False)
    amount = models.IntegerField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.slug or "Space paid"

def spaceuserpayment_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(spaceuserpayment_pre_save_receiver, sender=SpaceUserPayment)


class StaffMembersModel(models.Model):
    name = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True)
    company = models.ForeignKey(SpaceusersModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug


def staffmember_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(staffmember_pre_save_receiver, sender=StaffMembersModel)


# Events Model
class EventsModel(models.Model):
    name = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(blank=True, null=True)
    event_date = models.DateTimeField(auto_now_add=False)
    description = models.TextField(blank=True)
    itenary = models.TextField(blank=True)
    is_physical = models.BooleanField(default=True)

    def __str__(self):
        return self.slug


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(event_pre_save_receiver, sender=EventsModel)


class AttendeeModel(models.Model):
    events = models.ManyToManyField(EventsModel)
    name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, blank=True)

    def __str__(self):
        return self.slug


def attendee_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(attendee_pre_save_receiver, sender=AttendeeModel)


# Tutoring models
class CourseModel(models.Model):
    name = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.slug


def course_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(course_pre_save_receiver, sender=CourseModel)


class Facilitator(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    agreement_doc = models.FileField(
        upload_to=f'facilitators/{name}/', blank=True, null=True)
    courses = models.ManyToManyField(CourseModel)

    def __str__(self):
        return self.slug


def facilitator_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(facilitator_pre_save_receiver, sender=Facilitator)


class StudentsModel(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    courses = models.ManyToManyField(CourseModel)

    def __str__(self):
        return self.slug


def student_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(student_pre_save_receiver, sender=StudentsModel)


class StudentPayment(models.Model):
    student = models.ForeignKey(StudentsModel, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120, blank=True,null=True)
    slug = models.SlugField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=False)
    amount = models.IntegerField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.slug or "student paid"

def studentpayment_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(studentpayment_pre_save_receiver, sender=StudentPayment)




class OfficialDoc(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    file = models.FileField(upload_to='officedocs/', blank=True)

    def __str__(self):
        return self.slug

def officialdoc_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(officialdoc_pre_save_receiver, sender=OfficialDoc)

