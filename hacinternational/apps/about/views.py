from django.views.generic import TemplateView


class WhoWeAreView(TemplateView):
    template_name = 'pages/who_we_are.html'


class MeetTheTeamView(TemplateView):
    template_name = 'pages/meet_the_team.html'
