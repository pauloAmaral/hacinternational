from django.http import Http404
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


class EventView(TemplateView):
    template_name = 'pages/event.html'

    def get(self, request, event_id, *args, **kwargs):
        try:
            event = Event.active_objects.get(id=event_id)
        except Event.DoesNotExist:
            raise Http404('No VolunteerOpportunity matches the given query.')

        ctx = {
            'event': event
        }

        return render(request, self.template_name, ctx)
