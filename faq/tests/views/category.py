from django.test import TestCase, Client
from django.urls import reverse

from faq.views.category import CategoryView
from faq.models import Category

from model_bakery import baker


class TestCategoryView(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.view = CategoryView()
        cls.user = baker.make('User')
        cls.client = Client()

    def test_get_context_data_with_existing_category_kwargs(self):
        category = Category.objects.first()
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('faq:category', kwargs={'id': category.id}),
        )
        self.assertIn('category', response.context)
        self.assertEqual(response.context['category'], category)

# EOF