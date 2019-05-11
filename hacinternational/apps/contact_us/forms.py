from django import forms


class ContactUsForm(forms.Form):
    subject = forms.CharField(max_length=500)
    email_address = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
