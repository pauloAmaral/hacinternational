from django.conf import settings
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.views.generic import FormView, TemplateView

from . import forms


class ContactUsView(FormView):
    template_name = 'pages/contact_us/form.html'
    form_class = forms.ContactUsForm
    success_url = reverse_lazy('contact_us_success')

    def get_initial(self):
        initial = super(ContactUsView, self).get_initial()

        if self.request.GET.get('subject'):
            initial['subject'] = self.request.GET['subject']

        return initial

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        email = EmailMessage(
            from_email=form.cleaned_data['email_address'],
            to=(settings.CONTACT_EMAIL,),
            subject=form.cleaned_data['subject'],
            body=form.cleaned_data['message'])

        email.send(fail_silently=False)
        return super(ContactUsView, self).form_valid(form)


class ContactUsSuccessView(TemplateView):
    template_name = 'pages/contact_us/form_success.html'
