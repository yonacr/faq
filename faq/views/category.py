from django.views.generic import TemplateView

from faq.models import Category


class CategoryView(TemplateView):
    """A view that displays a Category with its related Questions and Answers."""

    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs.get('id'))
        return context

# EOF
