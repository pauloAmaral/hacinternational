from django.db import models
from ckeditor.fields import RichTextField

from hacinternational.apps.base_model import BaseModel


DURATION_CHOICES = (
    ('short_term', 'Short Term'),
    ('long_term', 'Long Term')
)


class VolunteerOpportunityActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class VolunteerOpportunity(BaseModel):
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Volunteering opportunity'
        verbose_name_plural = 'Volunteering opportunities'

    objects = models.Manager()
    active_objects = VolunteerOpportunityActiveManager()

    is_active = models.BooleanField(
        default=True,
        help_text='If not active, it will not be shown on the list of '
                  'available opportunities')
    title = models.CharField(
        max_length=255,
        help_text='Main title for the volunteering opportunity')
    location = models.CharField(
        max_length=255,
        help_text='Where the volunteering opportunity will take place')
    duration = models.CharField(
        max_length=20, choices=DURATION_CHOICES, default=DURATION_CHOICES[0][0],
        help_text='How long the volunteering opportunity will take')
    description = RichTextField(
        help_text='What the volunteer will need to do (What will you be doing?)'
    )
    volunteer_profile = RichTextField(
        help_text='What kind of volunteer we are looking for '
                  '(Who are we looking for?)')
    reason = RichTextField(
        help_text='Why this is important (Why will you want to do this?)',
        null=True, blank=False)
    rewards = RichTextField(
        help_text='What the volunteer will get for doing this '
                  '(What will you get from this opportunity?)',
        null=True, blank=False)

    def __str__(self):
        return self.title
