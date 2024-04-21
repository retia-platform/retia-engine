from django.contrib import admin

from retia_api.databases.models import ActivityLog, Detector, Device

admin.site.register(Device)
admin.site.register(Detector)
admin.site.register(ActivityLog)
