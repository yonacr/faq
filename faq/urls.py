from django.urls import path, include

from faq.views.category import CategoryView, CategoryListView
from faq.views.question import QuestionListView, QuestionUpdateView, QuestionCreateView
from faq.api import CategoryViewSet, QuestionViewSet
from rest_framework import routers

app_name = 'faq'

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'question', QuestionViewSet)


urlpatterns = [
    path('category/<int:id>', CategoryView.as_view(), name='category'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('questions/', QuestionListView.as_view(), name='question_list'),
    path('question/update/<int:id>', QuestionUpdateView.as_view(), name='question_update'),
    path('question/create/', QuestionCreateView.as_view(), name='question_create'),
    path('api/v1/', include(router.urls)),
]



# EOF
