from django.conf.urls import patterns, url
from kanisa.views.xhr.pages import (CreatePageView,
                                    ListPagesView)
from kanisa.views.xhr.sermons import MarkSermonSeriesCompleteView
from kanisa.views.xhr.diary import (ScheduleRegularEventView,
                                    DiaryGetSchedule)
from kanisa.views.xhr.media import (InlineImagesListView,
                                    InlineImagesDetailView)
from kanisa.views.xhr.navigation import (ListNavigationView,
                                         MoveNavigationElementDownView,
                                         MoveNavigationElementUpView)
from kanisa.views.xhr.users import AssignPermissionView


urlpatterns = patterns('',
                       url(r'^permissions/$',
                           AssignPermissionView.as_view(),
                           {},
                           'kanisa_manage_xhr_assign_permission'),
                       url(r'^navigation/list/$',
                           ListNavigationView.as_view(),
                           {},
                           'kanisa_manage_xhr_list_navigation'),
                       url(r'^navigation/up/$',
                           MoveNavigationElementUpView.as_view(),
                           {},
                           'kanisa_manage_xhr_navigation_up'),
                       url(r'^navigation/down/$',
                           MoveNavigationElementDownView.as_view(),
                           {},
                           'kanisa_manage_xhr_navigation_down'),
                       url(r'^pages/create/$',
                           CreatePageView.as_view(),
                           {},
                           'kanisa_manage_xhr_create_page'),
                       url(r'^pages/list/$',
                           ListPagesView.as_view(),
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
                           DiaryGetSchedule.as_view(),
                           {},
                           'kanisa_manage_xhr_diary_get_schedule'),
                       url(r'^media/images/$',
                           InlineImagesListView.as_view(),
                           {},
                           'kanisa_manage_xhr_media_inline_images'),
                       url(r'^media/images/(?P<pk>\d+)$',
                           InlineImagesDetailView.as_view(),
                           {},
                           'kanisa_manage_xhr_media_inline_images_detail'),
                       )
