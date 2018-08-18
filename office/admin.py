from django.contrib import admin

from .models import (Appointment, Appointee)


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_time', 'end_time', 'appointment_date', 'attending', 'appointee']

admin.site.register(Appointment, AppointmentAdmin)


class AppointeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'designation', 'start_time', 'end_time', 'responsibility', 'photo']

admin.site.register(Appointee, AppointeeAdmin)
