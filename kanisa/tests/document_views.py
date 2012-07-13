from django.core.urlresolvers import reverse
from kanisa.tests.utils import KanisaViewTestCase


class DocumentManagementViewTest(KanisaViewTestCase):
    def test_views_protected(self):
        self.check_staff_only(reverse('kanisa_manage_documents'))
        self.check_staff_only(reverse('kanisa_manage_documents_create'))
        self.check_staff_only(reverse('kanisa_search_documents'))

        # These would 404 if you were logged in
        self.check_staff_only(reverse('kanisa_manage_documents_update', args=[1, ]))
        self.check_staff_only(reverse('kanisa_manage_documents_delete', args=[1, ]))