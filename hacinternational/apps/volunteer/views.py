from django.shortcuts import render
from django.views.generic import TemplateView

from hacinternational.apps.volunteer.models import VolunteerOpportunity


class VolunteerListView(TemplateView):
    template_name = 'pages/volunteer/list.html'

    def get(self, request, *args, **kwargs):
        opportunities = VolunteerOpportunity.objects.filter(is_active=True)

        ctx = {
            'opportunities': opportunities
        }

        return render(request, self.template_name, ctx)
