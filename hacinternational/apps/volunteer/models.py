from django.db import models

from hacinternational.apps.base_model import BaseModel


DURATION_CHOICES = (
    ('short_term', 'Short Term'),
    ('long_term', 'Long Term')
)


class VolunteerOpportunity(BaseModel):
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
    description = models.CharField(
        max_length=1500, help_text='What the volunteer will need to do')
    volunteer_profile = models.CharField(
        max_length=500, help_text='What kind of volunteer we are looking for',
        null=True, blank=False)
    reason = models.CharField(
        max_length=500, help_text='Why this is important', null=True,
        blank=False)
    rewards = models.CharField(
        max_length=500, help_text='What the volunteer will get for doing this',
        null=True, blank=False)

    def __str__(self):
        return self.title
