from django.shortcuts import render
from django.views.generic import TemplateView

from hacinternational.apps.volunteer.models import VolunteerOpportunity


class VolunteerListView(TemplateView):
    template_name = 'pages/volunteer/list.html'

    def get(self, request, *args, **kwargs):
        opportunities = VolunteerOpportunity.active_objects.all()

        ctx = {
            'opportunities': opportunities
        }

        return render(request, self.template_name, ctx)


class VolunteerOpportunityView(TemplateView):
    template_name = 'pages/volunteer/opportunity.html'

    def get(self, request, id, *args, **kwargs):
        opportunity = VolunteerOpportunity.active_objects.get(id=id)

        ctx = {
            'opportunity': opportunity
        }

        return render(request, self.template_name, ctx)
