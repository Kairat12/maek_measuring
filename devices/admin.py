from django.contrib import admin

from devices.models import Device


# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    search_fields = ['name']
