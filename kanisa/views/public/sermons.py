from django.core.urlresolvers import reverse
from django.db.models import F
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import (
    DetailView,
    ListView,
    RedirectView,
    TemplateView
)
from kanisa.models import Sermon, SermonSeries


class SermonIndexView(TemplateView):
    template_name = 'kanisa/public/sermons/index.html'

    def get_context_data(self, **kwargs):
        context = super(SermonIndexView,
                        self).get_context_data(**kwargs)

        series = SermonSeries.objects.filter(active=True)
        context['active_series'] = series
        latest_sermons = Sermon.preached_objects.all()
        context['latest_sermons'] = latest_sermons[:5]
        context['kanisa_title'] = 'Sermons'

        url = reverse('sermon_podcast_itunes')
        absolute_url = self.request.build_absolute_uri(url)
        context['podcast_url'] = absolute_url

        return context


class SermonSeriesDetailView(DetailView):
    model = SermonSeries
    template_name = 'kanisa/public/sermons/series.html'

    def get_context_data(self, **kwargs):
        context = super(SermonSeriesDetailView,
                        self).get_context_data(**kwargs)
        context['kanisa_title'] = unicode(self.object)
        return context


class SermonDetailView(DetailView):
    template_name = 'kanisa/public/sermons/sermon.html'

    def get_queryset(self):
        return Sermon.preached_objects.all()

    def get_context_data(self, **kwargs):
        context = super(SermonDetailView, self).get_context_data(**kwargs)
        context['kanisa_title'] = unicode(self.object)
        return context

    def get_object(self, queryset=None):
        object = super(SermonDetailView, self).get_object(queryset)

        if 'series' not in self.kwargs:
            if object.series is not None:
                raise Http404
            return object

        if object.series.slug != self.kwargs['series']:
            raise Http404

        return object


class SermonArchiveView(ListView):
    model = Sermon
    template_name = 'kanisa/public/sermons/archive.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(SermonArchiveView,
                        self).get_context_data(**kwargs)

        context['kanisa_title'] = 'Sermon Archives'

        return context


class SermonBaseDownloadView(RedirectView):
    permanent = False

    def get_redirect_url(self, sermon_id):
        sermon = get_object_or_404(Sermon, pk=sermon_id)

        if not sermon.mp3_url():
            raise Http404

        sermon.downloads = F(self.count_field) + 1
        sermon.save()

        return sermon.mp3_url()


class SermonDownloadView(SermonBaseDownloadView):
    count_field = 'downloads'


class SermonPodcastDownloadView(SermonBaseDownloadView):
    count_field = 'podcast_downloads'
