from django.contrib import admin
from .models import Device, Detector, ActivityLog

admin.site.register(Device)
admin.site.register(Detector)
admin.site.register(ActivityLog)
