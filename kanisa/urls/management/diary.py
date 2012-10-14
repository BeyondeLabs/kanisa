from django.conf.urls import patterns, url
from kanisa.views.diary import (DiaryRegularEventCreateView,
                                DiaryRegularEventUpdateView,
                                DiaryRegularEventBulkEditView,
                                DiaryRegularEventsView,
                                DiaryEventIndexView,
                                DiaryScheduleRegularEventView,
                                DiaryCancelScheduledEventView,
                                DiaryScheduledEventCreateView,
                                DiaryScheduledEventUpdateView,
                                DiaryScheduledEventCloneView,
                                DiaryScheduleWeeksRegularEventView,
                                EventContactIndexView,
                                EventContactCreateView,
                                EventContactUpdateView)

urlpatterns = patterns('',
                       url(r'^$',
                           DiaryEventIndexView.as_view(),
                           {},
                           'kanisa_manage_diary'),
                       url(r'^regular/$',
                           DiaryRegularEventsView.as_view(),
                           {},
                           'kanisa_manage_diary_regularevents'),
                       url(r'^regular/create/$',
                           DiaryRegularEventCreateView.as_view(),
                           {},
                           'kanisa_manage_diary_regular_create'),
                       url(r'^regular/edit/(?P<pk>\d+)$',
                           DiaryRegularEventUpdateView.as_view(),
                           {},
                           'kanisa_manage_diary_regular_update'),
                       url(r'^regular/bulkedit/(?P<pk>\d+)/$',
                           DiaryRegularEventBulkEditView.as_view(),
                           {},
                           'kanisa_manage_diary_regular_bulkedit'),
                       url(r'^scheduled/create/$',
                           DiaryScheduledEventCreateView.as_view(),
                           {},
                           'kanisa_manage_diary_scheduled_create'),
                       url(r'^scheduled/edit/(?P<pk>\d+)$',
                           DiaryScheduledEventUpdateView.as_view(),
                           {},
                           'kanisa_manage_diary_scheduled_update'),
                       url(r'^schedule/(?P<pk>\d+)/(?P<thedate>\d{8})/$',
                           DiaryScheduleRegularEventView.as_view(),
                           {},
                           'kanisa_manage_diary_schedule_regular_event'),
                       url(r'^schedule/all/$',
                           DiaryScheduleWeeksRegularEventView.as_view(),
                           {},
                           'kanisa_manage_diary_schedule_weeks_regular_event'),
                       url(r'^cancel/(?P<pk>\d+)/$',
                           DiaryCancelScheduledEventView.as_view(),
                           {},
                           'kanisa_manage_diary_cancel_scheduled_event'),
                       url(r'^clone/$',
                           DiaryScheduledEventCloneView.as_view(),
                           {},
                           'kanisa_manage_diary_clone_scheduled_event'),
                       url(r'^contacts/$',
                           EventContactIndexView.as_view(),
                           {},
                           'kanisa_manage_diary_contacts'),
                       url(r'^contacts/create/$',
                           EventContactCreateView.as_view(),
                           {},
                           'kanisa_manage_diary_contacts_create'),
                       url(r'^contacts/edit/(?P<pk>\d+)$',
                           EventContactUpdateView.as_view(),
                           {},
                           'kanisa_manage_diary_contacts_update'),
                       )
