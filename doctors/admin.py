from django.contrib import admin
from .models import Specialty, DoctorProfile, WorkingSchedule

admin.site.register(Specialty)
admin.site.register(DoctorProfile)
admin.site.register(WorkingSchedule)