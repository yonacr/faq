from django.test import TestCase, Client
from django.urls import reverse

from faq.views.category import CategoryView

from model_bakery import baker


class TestCategoryView(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.view = CategoryView()
        cls.user = baker.make('User')
        cls.client = Client()
        # TODO: test for permission access

    def test_get_context_data_with_existing_category_kwargs(self):
        category = baker.make('Category')
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('faq:category', kwargs={'id': 1}),
        )
        self.assertIn('category', response.context)
        self.assertEqual(response.context['category'], category)

# EOF