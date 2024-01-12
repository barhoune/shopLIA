from django.contrib import admin
from .models import Order
from django.contrib.admin.models import LogEntry
# Register your models here.
class orderAdmin(admin.ModelAdmin):
    list_display=['user','product','total']
    list_filter=['user',]
admin.site.register(Order,orderAdmin)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'user', 'action_time')

admin.site.register(LogEntry, LogEntryAdmin)