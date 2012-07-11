from django.conf.urls import patterns, url
from django.contrib.admin.views.decorators import staff_member_required as smr
from kanisa.views.social import (SocialIndexView,
                                 SocialTwitterIndexView,
                                 SocialTwitterPostView,
                                 ScheduledTweetCreateView,
                                 ScheduledTweetUpdateView)


urlpatterns = patterns('',
                       url(r'^$',
                           smr(SocialIndexView.as_view()),
                           {},
                           'kanisa_manage_social'),
                       url(r'^twitter/$',
                           smr(SocialTwitterIndexView.as_view()),
                           {},
                           'kanisa_manage_social_twitter'),
                       url(r'^twitter/scheduled/create/$',
                           smr(ScheduledTweetCreateView.as_view()),
                           {},
                           'kanisa_manage_social_twitter_create'),
                       url(r'^twitter/scheduled/edit/(?P<pk>\d+)$',
                           smr(ScheduledTweetUpdateView.as_view()),
                           {},
                           'kanisa_manage_social_twitter_update'),
                       url(r'^twitter/post/$',
                           smr(SocialTwitterPostView.as_view()),
                           {},
                           'kanisa_manage_social_twitter_post'),
                       )
