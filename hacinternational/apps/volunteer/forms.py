from django import forms

from hacinternational.apps.volunteer.models import VolunteerOpportunity


class VolunteerOpportunityForm(forms.ModelForm):
    class Meta:
        model = VolunteerOpportunity
        fields = '__all__'
        verbose_name = 'Volunteering opportunity'
        verbose_name_plural = 'Volunteering opportunities'

    description = forms.CharField(
        widget=forms.Textarea(),
        help_text='What the volunteer will need to do')
    volunteer_profile = forms.CharField(
        widget=forms.Textarea(), required=False,
        help_text='What kind of volunteer we are looking for')
    reason = forms.CharField(
        widget=forms.Textarea(), required=False,
        help_text='Why this is important')
    rewards = forms.CharField(
        widget=forms.Textarea(), required=False,
        help_text='What the volunteer will get for doing this')
