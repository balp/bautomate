from bautomate.models import TelldusDevice, Group
from django.contrib import admin

class TelldusDeviceAdmin(admin.ModelAdmin):
    list_display = ('td_id', 'name', 'on')

admin.site.register(TelldusDevice, TelldusDeviceAdmin)
admin.site.register(Group)
