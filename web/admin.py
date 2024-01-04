from django.contrib import admin
from web.models import Event


class EventAdmin(admin.ModelAdmin):
    ...


admin.site.register(Event, EventAdmin)
