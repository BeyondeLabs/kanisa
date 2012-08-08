from django.conf.urls import patterns, url
from kanisa.views.xhr import (ScheduleRegularEventView,
                              CreatePageView,
                              MarkSermonSeriesCompleteView)

urlpatterns = patterns('',
                       url(r'^permissions/$',
                           'kanisa.views.xhr.assign_permission',
                           {},
                           'kanisa_manage_xhr_assign_permission'),
                       url(r'^pages/create/$',
                           CreatePageView.as_view(),
                           {},
                           'kanisa_manage_xhr_create_page'),
                       url(r'^pages/list/$',
                           'kanisa.views.xhr.list_pages',
                           {},
                           'kanisa_manage_xhr_list_pages'),
                       url(r'^sermons/markcomplete/$',
                           MarkSermonSeriesCompleteView.as_view(),
                           {},
                           'kanisa_manage_xhr_sermon_series_complete'),
                       url(r'^diary/schedule/update/$',
                           ScheduleRegularEventView.as_view(),
                           {},
                           'kanisa_manage_xhr_diary_schedule_regular'),
                       url(r'^diary/schedule/fetch/(?P<date>\d+)/$',
                           'kanisa.views.xhr.get_events',
                           {},
                           'kanisa_manage_xhr_diary_get_schedule'),
                       )
