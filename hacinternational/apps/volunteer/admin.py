from django.contrib import admin

from hacinternational.apps.volunteer.forms import VolunteerOpportunityForm
from hacinternational.apps.volunteer.models import VolunteerOpportunity


@admin.register(VolunteerOpportunity)
class VolunteerOpportunityAdmin(admin.ModelAdmin):
    form = VolunteerOpportunityForm
    list_display = ['title', 'is_active', 'created_at']
