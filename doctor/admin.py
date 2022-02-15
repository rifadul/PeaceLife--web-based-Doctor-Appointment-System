from django.contrib import admin
from .models import Department, Doctor, DoctorSchedule
# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    '''Admin View for BlogPost'''

    list_display = ('id','full_name',)


@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    '''Admin View for BlogPost'''

    list_display = ('user', 'day', 'start_time', 'end_time')
