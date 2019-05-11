from django.views.generic import TemplateView


class DonateView(TemplateView):
    template_name = 'pages/donate.html'
