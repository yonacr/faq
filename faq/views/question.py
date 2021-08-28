from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView

from django.views.generic.base import View

from faq.forms.question import QuestionUpdateForm, QuestionCreateForm
from faq.forms.answer import AnswerCreateForm
from faq.models import Question


class QuestionListView(LoginRequiredMixin, TemplateView):
    """
    A view that displays all questions
    """

    template_name = "question_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "answered": Question.objects.exclude(answer=None).order_by('creation_date'),
            "unanswered": Question.objects.filter(answer=None).order_by('creation_date')
        })
        return context


class QuestionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    A view that allows to update a question's category,
    and create/update its related answer
    """

    template_name = "question_update.html"
    success_url = reverse_lazy('faq:question_list')
    permission_required = ('faq.change_question')

    def get(self, request, **kwargs):
        question = Question.objects.get(id=kwargs['id'])
        context = {
            'question_form': QuestionUpdateForm(instance=question),
            'question': question
        }
        if question.answer:
            context['answer_form'] = AnswerCreateForm(instance=question.answer)
        else:
            context['answer_form'] = AnswerCreateForm()
        return render(request, "question_update.html", context)

    def post(self, request, **kwargs):
        question = Question.objects.get(id=kwargs['id'])
        if question.answer:
            answer_form = AnswerCreateForm(request.POST, instance=question.answer)
        else:
            answer_form = AnswerCreateForm(request.POST)
        question_form = QuestionUpdateForm(request.POST)

        if answer_form.is_valid() and question_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.author = self.request.user
            answer.save()
            question = question_form.save(commit=False)
            question.answer = answer
            question.save()

        messages.success(request, "Réponse enregistrée")
        return redirect(reverse('faq:question_list'))


class QuestionCreateView(LoginRequiredMixin, FormView):
    """
    A view for asking a Question
    """

    form_class = QuestionCreateForm
    template_name = "question_create.html"
    success_url = reverse_lazy('faq:category_list')

    def form_valid(self, form):
        Question.objects.create(
            text=form.cleaned_data['text'],
            author=self.request.user,
        )
        messages.success(
            self.request,
            "Votre question a été soumise aux administrateurs"
        )
        return super().form_valid(form)

# EOF


