from django.core.urlresolvers import reverse
from kanisa.forms import DocumentForm
from kanisa.models import Document
from kanisa.views.generic import (KanisaCreateView, KanisaUpdateView,
                                  KanisaListView)


class DocumentBaseView:
    kanisa_lead = ('Storing documents on your site allows people to have '
                   'easy access to the files they need.')

    def get_kanisa_root_crumb(self):
        return {'text': 'Documents',
                'url': reverse('kanisa_manage_documents')}


class DocumentIndexView(KanisaListView, DocumentBaseView):
    model = Document
    queryset = Document.objects.all()

    template_name = 'kanisa/management/documents/index.html'
    kanisa_title = 'Manage Documents'
    kanisa_is_root_view = True


class DocumentCreateView(KanisaCreateView, DocumentBaseView):
    form_class = DocumentForm
    template_name = 'kanisa/management/create.html'
    kanisa_title = 'Upload a Document'

    def get_success_url(self):
        return reverse('kanisa_manage_documents')


class DocumentUpdateView(KanisaUpdateView, DocumentBaseView):
    form_class = DocumentForm
    template_name = 'kanisa/management/create.html'
    model = Document

    def get_kanisa_title(self):
        return 'Edit Document: %s' % unicode(self.object)

    def get_success_url(self):
        return reverse('kanisa_manage_documents')
