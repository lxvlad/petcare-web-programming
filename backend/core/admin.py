from django.contrib import admin
from .models import Pet,Vaccination,Appointment,Note
admin.site.register(Pet);admin.site.register(Vaccination);admin.site.register(Appointment);admin.site.register(Note)
