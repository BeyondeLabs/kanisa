from django.views.generic import (
    DetailView,
    ListView,
    YearArchiveView,
)
from kanisa.models import BlogPost


class BlogMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BlogMixin, self).get_context_data(**kwargs)
        dates = BlogPost.published_objects.dates(
            'publish_date',
            'year'
        )
        context['years'] = [d.year for d in dates]
        return context


class BlogIndexView(BlogMixin, ListView):
    template_name = 'kanisa/public/blog/index.html'
    queryset = BlogPost.published_objects.all()


class BlogYearView(BlogMixin, YearArchiveView):
    queryset = BlogPost.published_objects.all()
    template_name = 'kanisa/public/blog/year.html'
    date_field = 'publish_date'
    make_object_list = True


class BlogPostDetailView(BlogMixin, DetailView):
    queryset = BlogPost.published_objects.all()
    template_name = 'kanisa/public/blog/post.html'

    def get_queryset(self):
        qs = super(BlogPostDetailView, self).get_queryset()
        qs = qs.filter(publish_date__year=self.kwargs['year'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(BlogPostDetailView, self).get_context_data(**kwargs)

        try:
            next_post = self.object.get_next_by_publish_date()
        except BlogPost.DoesNotExist:
            next_post = None

        try:
            previous_post = self.object.get_previous_by_publish_date()
        except BlogPost.DoesNotExist:
            previous_post = None

        context['next'] = next_post
        context['previous'] = previous_post

        return context