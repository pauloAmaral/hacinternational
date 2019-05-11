from django.contrib import admin

from hacinternational.apps.events.forms import EventForm
from hacinternational.apps.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = ['title', 'is_active', 'created_at']
