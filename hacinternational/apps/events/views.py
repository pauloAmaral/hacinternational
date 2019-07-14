from django.shortcuts import render
from django.views.generic import TemplateView

from hacinternational.apps.events.models import Event


class EventsView(TemplateView):
    template_name = 'pages/events.html'

    def get(self, request, *args, **kwargs):
        events = Event.active_objects.all()

        ctx = {
            'events': events
        }

        return render(request, self.template_name, ctx)
