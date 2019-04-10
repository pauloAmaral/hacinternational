"""hacinternational URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from collections import OrderedDict

from django.conf.urls import url
from django.contrib import admin, sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path, reverse

from hacinternational.apps.about.views import WhoWeAreView, MeetTheTeamView
from hacinternational.apps.home.views import HomeView



# class StaticViewSitemap(sitemaps.Sitemap):
#     priority = 0.5
#     changefreq = 'weekly'
#
#     def items(self):
#         return ['home']
#
#     def location(self, item):
#         return reverse(item)
#
#
# sitemaps = OrderedDict([
#     ('static', StaticViewSitemap),
# ])


urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    #     name='django.contrib.sitemaps.views.sitemap'),

    path('', HomeView.as_view(), name='home'),
    path('who-we-are/', WhoWeAreView.as_view(), name='who_we_are'),
    path('meet-the-team/', MeetTheTeamView.as_view(), name='meet_the_team')
]
