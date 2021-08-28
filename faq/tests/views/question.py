from django.test import TestCase, Client
from django.urls import reverse

from model_bakery import baker


class TestQuestionListView(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.user = baker.make('User')


    def test_get_context_data(self):
        unanswered = baker.make('Question')
        answer = baker.make('Answer')
        answered = baker.make('Question', answer=answer)

        self.client.force_login(self.user)
        response = self.client.get(
            reverse('faq:question_list'),
        )
        self.assertIn('answered', response.context)
        self.assertIn(answered, response.context['answered'])
        self.assertIn('unanswered', response.context)
        self.assertIn(unanswered, response.context['unanswered'])

# EOF
