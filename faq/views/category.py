from django.views.generic import TemplateView, ListView

from faq.models import Category, Question


class CategoryView(TemplateView):
    """A view that displays a Category with its related Questions and Answers."""

    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs.get('id'))
        return context


class CategoryListView(ListView):

    model = Category
    template_name = "category_list.html"

# EOF
