from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, ListView, TemplateView, UpdateView
from django.views.generic.base import View

from faq.forms.question import QuestionUpdateForm
from faq.forms.answer import AnswerCreateForm
from faq.models import Question


class QuestionListView(TemplateView):
    """
    A view that displays all questions
    """

    template_name = "question_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "answered": Question.objects.exclude(answer=None),
            "unanswered": Question.objects.filter(answer=None)
        })
        return context


class QuestionUpdateView(View):
    """
    A view that allows to update a question's category,
    and create/update its related answer
    """

    template_name = "question_update.html"
    success_url = reverse_lazy('faq:question_list')

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
        if answer_form.is_valid():
            messages.info(request, "Answer is valid")
        if question_form.is_valid():
            messages.info(request, "Question is valid")

        if answer_form.is_valid() and question_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.author = self.request.user
            answer.save()
            question = question_form.save(commit=False)
            question.answer = answer
            question.save()

        messages.success(request, "Réponse enregistrée")
        return redirect(reverse('faq:question_list'))

# EOF


