from django.urls import path

from faq.views.category import CategoryView

app_name = 'faq'

urlpatterns = [
    path('category/<int:id>', CategoryView.as_view(), name='category')
]

# EOF
