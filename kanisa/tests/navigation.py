from django.core.exceptions import ValidationError
from django.test import TestCase
from kanisa.models import NavigationElement
import factory


class NavigationFactory(factory.Factory):
    FACTORY_FOR = NavigationElement
    title = 'Title'


class NavigationElementTest(TestCase):
    def test_unicode(self):
        n = NavigationFactory.build()
        self.assertEqual(unicode(n), 'Title')

    def test_navigation_element_cannot_be_its_own_parent(self):
        n = NavigationFactory.create()
        n.parent = n

        with self.assertRaises(ValidationError) as cm:
            n.full_clean()

        errors = cm.exception.message_dict
        self.assertTrue('parent' in errors)
        self.assertEqual(errors['parent'],
                         ['A navigation element cannot be its own parent.', ])

    def test_navigation_element_cannot_have_child_as_parent(self):
        parent = NavigationFactory.create()
        child = NavigationFactory.create(parent=parent)

        parent.parent = child

        with self.assertRaises(ValidationError) as cm:
            parent.full_clean()

        errors = cm.exception.message_dict
        self.assertTrue('parent' in errors)
        self.assertEqual(errors['parent'],
                         ['Invalid parent - cyclical hierarchy '
                          'detected.', ])

    def test_move_down_sole_element(self):
        element = NavigationFactory.create()

        with self.assertRaises(NavigationElement.DoesNotExist):
            element.move_down()

    def test_move_down_non_sole_element(self):
        element = NavigationFactory.create()
        sibling = NavigationFactory.create(title="ZTitle")

        element.move_down()

        pks = [n.pk for n in NavigationElement.objects.all()]

        self.assertEqual(pks, [sibling.pk, element.pk])

        element = NavigationElement.objects.get(pk=element.pk)
        sibling = NavigationElement.objects.get(pk=sibling.pk)

        sibling.move_down()

        pks = [n.pk for n in NavigationElement.objects.all()]

        self.assertEqual(pks, [element.pk, sibling.pk])

    def test_move_up_sole_element(self):
        element = NavigationFactory.create()

        with self.assertRaises(NavigationElement.DoesNotExist):
            element.move_up()

    def test_move_up_non_sole_element(self):
        element = NavigationFactory.create()
        sibling = NavigationFactory.create(title="ZTitle")

        sibling.move_up()

        pks = [n.pk for n in NavigationElement.objects.all()]

        self.assertEqual(pks, [sibling.pk, element.pk])

        element = NavigationElement.objects.get(pk=element.pk)
        sibling = NavigationElement.objects.get(pk=sibling.pk)

        element.move_up()

        pks = [n.pk for n in NavigationElement.objects.all()]

        self.assertEqual(pks, [element.pk, sibling.pk])
