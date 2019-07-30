import datetime

from django.db import models
from ckeditor.fields import RichTextField

from hacinternational.apps.base_model import BaseModel


class EventActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                models.Q(is_active=True) &
                models.Q(
                    models.Q(date__gte=datetime.datetime.now().date()) |
                    models.Q(date__isnull=True)
                )
        )


class Event(BaseModel):
    class Meta:
        ordering = ('date', 'created_at',)

    objects = models.Manager()
    active_objects = EventActiveManager()

    is_active = models.BooleanField(
        default=True,
        help_text='If not active, it will not be shown on the list of '
                  'current events')
    title = models.CharField(
        max_length=255, help_text='Title of the event')
    image = models.ImageField()
    date = models.DateField(
        help_text='Date of the event (if empty, will show TBA)',
        null=True, blank=False)
    location = models.CharField(
        max_length=255,
        help_text='Where the event will take place')
    description = RichTextField(
        help_text='Description of the event')
