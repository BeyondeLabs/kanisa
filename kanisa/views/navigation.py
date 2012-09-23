from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from kanisa.forms.navigation import NavigationElementForm
from kanisa.models import NavigationElement
from kanisa.views.generic import (KanisaAuthorizationMixin,
                                  KanisaListView,
                                  KanisaCreateView,
                                  KanisaUpdateView)


class NavigationElementBaseView(KanisaAuthorizationMixin):
    kanisa_lead = ('Navigation elements appear in the navigation bar at the '
                   'top of every page.')
    kanisa_root_crumb = {'text': 'Navigation',
                         'url': reverse_lazy('kanisa_manage_navigation')}
    permission = 'kanisa.manage_navigation'
    kanisa_nav_component = 'navigation'


class NavigationElementIndexView(NavigationElementBaseView,
                                 KanisaListView):
    model = NavigationElement

    template_name = 'kanisa/management/navigation/index.html'
    kanisa_title = 'Manage Navigation'
    kanisa_is_root_view = True


class NavigationElementCreateView(NavigationElementBaseView,
                                  KanisaCreateView):
    form_class = NavigationElementForm
    kanisa_title = 'Create Navigation Element'
    success_url = reverse_lazy('kanisa_manage_navigation')


class NavigationElementUpdateView(NavigationElementBaseView,
                                  KanisaUpdateView):
    form_class = NavigationElementForm
    model = NavigationElement
    success_url = reverse_lazy('kanisa_manage_navigation')


class NavigationElementMoveDownView(NavigationElementBaseView,
                                    RedirectView):
    permanent = False

    def get_redirect_url(self, pk):
        element = get_object_or_404(NavigationElement, pk=pk)

        try:
            element.move_down()
        except NavigationElement.DoesNotExist:
            raise Http404

        message = "Moved '%s' down." % element
        messages.success(self.request, message)

        return reverse('kanisa_manage_navigation')


class NavigationElementMoveUpView(NavigationElementBaseView,
                                  RedirectView):
    permanent = False

    def get_redirect_url(self, pk):
        element = get_object_or_404(NavigationElement, pk=pk)

        try:
            element.move_up()
        except NavigationElement.DoesNotExist:
            raise Http404

        message = "Moved '%s' up." % element
        messages.success(self.request, message)

        return reverse('kanisa_manage_navigation')