from django.conf.urls import patterns, include, url
from kanisa.views import KanisaIndexView
from kanisa.views.public.seasonal import seasonal_view


urlpatterns = patterns(
    '',
    url(r'^$', KanisaIndexView.as_view(), {}, 'kanisa_public_index'),
    url(r'^banners/', include('kanisa.urls.public.banners')),
    url(r'^blog/', include('kanisa.urls.public.blog')),
    url(r'^christmas/$', seasonal_view, {'season': 'christmas'},
        'kanisa_public_seasonal'),
    url(r'^diary/', include('kanisa.urls.public.diary')),
    url(r'^easter/$', seasonal_view, {'season': 'easter'},
        'kanisa_public_seasonal'),
    url(r'^manage/', include('kanisa.urls.management')),
    url(r'^members/', include('kanisa.urls.members')),
    url(r'^search/', include('kanisa.urls.public.search')),
    url(r'^sermons/', include('kanisa.urls.public.sermons')),
    url(r'^xhr/', include('kanisa.urls.xhr')),
)
