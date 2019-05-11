import datetime

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from ckeditor.widgets import CKEditorWidget

from hacinternational.apps.events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    date = forms.DateField(
        widget=AdminDateWidget(),
        help_text='Date of the event (if empty, will show TBA)', required=False)
    description = forms.CharField(
        widget=CKEditorWidget(), help_text='Description of the event')

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")

        return date
