from django.conf.urls import patterns, url

from social_community.views import get_feed

urlpatterns = patterns(
                #  feed
                '',
                url(r'^test/$', get_feed),
            )
