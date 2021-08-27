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


class TestQuestionUpdateView(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.user = baker.make('User')

    def test_post_new_answer(self):
        question = baker.make('Question')
        self.client.force_login(self.user)
        form_data = {
            'answer_text': "This is my answer",
            'question_category': baker.make('Category')
        }

        response = self.client.post(
            reverse('faq:question_update', kwargs={'id': question.id}),
            form_data=form_data
        )
        raise ValueError("sorry I don't know how to test the two forms together")

# EOF
