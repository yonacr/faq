# from django.test import TestCase
#
# from faq.views.index import IndexView
#
# from model_bakery import baker
#
# # Create your tests here.
# class TestIndexView(TestCase):
#
#     def setUp(self):
#         self.view = IndexView()
#
#     def test_get_categories_question_without_ansmer_is_excluded(self):
#         baker.make('Question')
#         self.assertFalse(self.view.get_categories())
#
#     def test_get_categories(self):
#         answer = baker.make('Answer')
#         question = baker.make('Question', answer=answer)
#         expected = {
#             question.category: [question]
#         }
#         self.assertEqual(expected, self.view.get_categories())
#
