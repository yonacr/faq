from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View

from faq.models import Category, Question


class CategoryView(LoginRequiredMixin, TemplateView):
    """A view that displays a Category with its related Questions and Answers."""

    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs.get('id'))
        return context


class CategoryListView(LoginRequiredMixin, View):
    """
    A view that displays all categories and a Question search bar
    """

    template_name = "category_list.html"

    def get(self, request, **kwargs):
        context = {
            'categories': Category.objects.all(),
            'kwargs': kwargs,
            'self_kwargs': request.GET.get('q', '')
        }
        if request.GET.get('q'):
            context['result'] = Question.objects.filter(
                text__icontains=request.GET.get('q')
            )
        return render(request, self.template_name, context)

# EOF
