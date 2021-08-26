from django.contrib import admin
from django.urls import path

from faq.views.index import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    # path('admin/', FAQAdminView.as_view(), name="admin"),
    # path('category/<int>', CategoryView.as_view(), name='category'),
    # path('<int>/', Question)
]
