from django.urls import path

from faq.views.category import CategoryView, CategoryListView

app_name = 'faq'

urlpatterns = [
    path('category/<int:id>', CategoryView.as_view(), name='category'),
    path('category/', CategoryListView.as_view(), name='category_list')
]

# EOF
