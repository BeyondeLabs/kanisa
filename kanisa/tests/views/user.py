from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.auth.context_processors import PermWrapper
from django.core.cache import cache
from django.core import mail
from django.core.urlresolvers import reverse
from django.template import Context, Template
from django.template.loader import render_to_string
from kanisa.tests.utils import KanisaViewTestCase


class UserManagementViewTest(KanisaViewTestCase):
    def setUp(self):
        super(UserManagementViewTest, self).setUp()

        p = Permission.objects.get(codename='manage_users')
        fred = get_user_model().objects.get(username='fred')
        fred.user_permissions.add(p)
        fred.save()

    def test_views_protected(self):
        self.view_is_restricted(reverse('kanisa_manage_users'))
        self.view_is_restricted(reverse('kanisa_manage_users_activate',
                                        args=[1, ]))

    def test_base_view(self):
        self.client.login(username='fred', password='secret')
        resp = self.client.get(reverse('kanisa_manage_users'))
        self.assertEqual(resp.status_code, 200)

        self.assertTrue('user_list' in resp.context)

        bob = get_user_model().objects.get(username='bob')
        fred = get_user_model().objects.get(username='fred')
        superman = get_user_model().objects.get(username='superman')

        self.assertEqual(list(resp.context['user_list']),
                         [bob, fred, superman, ])

        self.client.logout()

    def test_template_complexity(self):
        tmpl = 'kanisa/management/users/_user_list.html'
        users = list(get_user_model().objects.all())
        user = get_user_model().objects.get(username='superman')
        perms = PermWrapper(user)

        with self.assertNumQueries(4):
            render_to_string(tmpl,
                             {'user_list': users,
                              'user': user,
                              'perms': perms})

    def test_template_tags(self):
        # To make sure this test is independent of other cached keys.
        cache.clear()

        def check_perm_template(request_user, user, perm):
            template = ("{%% load kanisa_tags %%}"
                        "{%% kanisa_user_has_perm '%s' %%}" % perm)
            t = Template(template)
            c = Context({"theuser": user, "user": request_user})
            return t.render(c)

        bob = get_user_model().objects.get(username='bob')
        fred = get_user_model().objects.get(username='fred')
        superman = get_user_model().objects.get(username='superman')

        # Fred has access to manage users, not to manage social
        # networks.
        with self.assertNumQueries(3):
            output = check_perm_template(superman, fred,
                                         'kanisa.manage_users')
            self.assertHTMLEqual(output,
                                 ('<input '
                                  'type="checkbox" '
                                  'checked="checked" '
                                  'class="kanisa_user_perm" '
                                  'data-permission-id="kanisa.manage_users" '
                                  'data-user-id="2" '
                                  'title="Can manage your users" '
                                  '/>'))

            output = check_perm_template(superman, fred,
                                         'kanisa.manage_social')

            self.assertHTMLEqual(output,
                                 ('<input '
                                  'type="checkbox" '
                                  'class="kanisa_user_perm" '
                                  'data-permission-id="kanisa.manage_social" '
                                  'data-user-id="2" '
                                  'title="Can manage your social networks" '
                                  '/>'))

        # Bob doesn't have access to either
        with self.assertNumQueries(2):
            output = check_perm_template(superman, bob,
                                         'kanisa.manage_users')
            self.assertHTMLEqual(output,
                                 ('<input '
                                  'type="checkbox" '
                                  'class="kanisa_user_perm" '
                                  'data-permission-id="kanisa.manage_users" '
                                  'data-user-id="1" '
                                  'title="Can manage your users" '
                                  '/>'))

            output = check_perm_template(superman, bob,
                                         'kanisa.manage_social')
            self.assertHTMLEqual(output,
                                 ('<input '
                                  'type="checkbox" '
                                  'class="kanisa_user_perm" '
                                  'data-permission-id="kanisa.manage_social" '
                                  'data-user-id="1" '
                                  'title="Can manage your social networks" '
                                  '/>'))

    def test_user_activate_view_user_already_active(self):
        self.client.login(username='fred', password='secret')

        bob = get_user_model().objects.get(username='bob')
        bob.is_active = True
        bob.save()

        url = reverse('kanisa_manage_users_activate', args=[bob.pk, ])
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)

        bob = get_user_model().objects.get(username='bob')
        self.assertTrue(bob.is_active)
        self.assertContains(resp, 'account is already active.')

        self.assertEqual(len(mail.outbox), 0)

        self.client.logout()

    def test_user_activate_view_on_inactive_user(self):
        self.client.login(username='fred', password='secret')

        bob = get_user_model().objects.get(username='bob')
        bob.is_active = False
        bob.save()

        url = reverse('kanisa_manage_users_activate', args=[bob.pk, ])
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)

        bob = get_user_model().objects.get(username='bob')
        self.assertTrue(bob.is_active)
        self.assertContains(resp, 'account is now activated.')

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['bob@example.com', ])
        self.assertEqual(mail.outbox[0].subject,
                         'Your Church Account Activated')

        self.client.logout()

    def test_user_activate_view_non_existent_user(self):
        self.client.login(username='fred', password='secret')
        url = reverse('kanisa_manage_users_activate', args=[1337, ])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        self.client.logout()

    def test_user_update_view_non_existent_user(self):
        self.client.login(username='fred', password='secret')
        url = reverse('kanisa_manage_users_update', args=[1337, ])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        self.client.logout()

    def test_user_update_view_get(self):
        self.client.login(username='fred', password='secret')

        bob = get_user_model().objects.get(username='bob')

        url = reverse('kanisa_manage_users_update', args=[bob.pk, ])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.client.logout()

    def test_user_update_view_post(self):
        self.client.login(username='fred', password='secret')

        bob = get_user_model().objects.get(username='bob')

        url = reverse('kanisa_manage_users_update', args=[bob.pk, ])
        resp = self.client.post(url, {'email': 'bob@example.net'},
                                follow=True)
        self.assertEqual(resp.status_code, 200)

        self.assertEqual([m.message for m in resp.context['messages']],
                         ['Registered User "bob" saved.', ])

        bob = get_user_model().objects.get(username='bob')
        self.assertEqual(bob.email, 'bob@example.net')

        self.client.logout()
