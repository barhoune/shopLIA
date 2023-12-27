from django.contrib import admin
from .models import Order
from django.contrib.admin.models import LogEntry
# Register your models here.
admin.site.register(Order)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'user', 'action_time')

admin.site.register(LogEntry, LogEntryAdmin)