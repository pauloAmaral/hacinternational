from django import forms
from ckeditor.widgets import CKEditorWidget

from hacinternational.apps.volunteer.models import VolunteerOpportunity


class VolunteerOpportunityForm(forms.ModelForm):
    class Meta:
        model = VolunteerOpportunity
        fields = '__all__'

    description = forms.CharField(
        widget=CKEditorWidget(),
        help_text='What the volunteer will need to do (What will you be doing?)'
    )
    volunteer_profile = forms.CharField(
        widget=CKEditorWidget(),
        help_text='What kind of volunteer we are looking for '
                  '(Who are we looking for?)')
    reason = forms.CharField(
        widget=CKEditorWidget(), required=False,
        help_text='Why this is important (Why will you want to do this?)')
    rewards = forms.CharField(
        widget=CKEditorWidget(), required=False,
        help_text='What the volunteer will get for doing this '
                  '(What will you get from this opportunity?)')
