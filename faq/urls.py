from django.urls import path

from faq.views.category import CategoryView, CategoryListView
from faq.views.question import QuestionListView, QuestionUpdateView, QuestionCreateView

app_name = 'faq'

urlpatterns = [
    path('category/<int:id>', CategoryView.as_view(), name='category'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('questions/', QuestionListView.as_view(), name='question_list'),
    path('question/update/<int:id>', QuestionUpdateView.as_view(), name='question_update'),
    path('question/create/', QuestionCreateView.as_view(), name='question_create')
]

# EOF
