from django.conf.urls import patterns, url
import kanisa.views.members.services as views
import kanisa.views.members.services.ccli as ccli_views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, {'show_all': False},
        'kanisa_members_services_index'),
    url(r'^all/$', views.index, {'show_all': True},
        'kanisa_members_services_index_all'),

    url(r'^service/(?P<service_pk>\d+)/$', views.service_detail, {},
        'kanisa_members_services_detail'),

    url(r'^songs/$', views.song_list, {},
        'kanisa_members_services_songs'),
    url(r'^songs/discover/$', views.song_discovery, {},
        'kanisa_members_services_song_discovery'),
    url(r'^songs/(?P<song_pk>\d+)/$', views.song_detail, {},
        'kanisa_members_services_song_detail'),

    url(r'^composers/(?P<composer_pk>\d+)/$', views.composer_detail, {},
        'kanisa_members_services_composer_detail'),

    url(r'^ccli/$', ccli_views.ccli_view, {},
        'kanisa_members_services_ccli'),
    url(r'^ccli/byusage/$', ccli_views.ccli_view, {'sort': 'usage'},
        'kanisa_members_services_ccli_by_usage'),
    url(r'^ccli/bytitle/$', ccli_views.ccli_view, {'sort': 'title'},
        'kanisa_members_services_ccli_by_title'),
)
