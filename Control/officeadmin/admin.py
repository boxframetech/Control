from django.contrib import admin
from .models import (
        SpacesModel,
    SpaceusersModel, 
        StaffMembersModel,
        EventsModel,
        AttendeeModel,
        CourseModel,
        Facilitator,
        StudentsModel,
        OfficialDoc,
        SpaceUserPayment,
        StudentPayment
        
        )

# Register your models here.
admin.site.register(SpacesModel)
admin.site.register(SpaceusersModel)
admin.site.register(SpaceUserPayment)
admin.site.register(StaffMembersModel)
admin.site.register(EventsModel)
admin.site.register(AttendeeModel)
admin.site.register(CourseModel)
admin.site.register(Facilitator)
admin.site.register(StudentsModel)
admin.site.register(StudentPayment)
admin.site.register(OfficialDoc)

