from django.contrib import admin

from faq.models import Question, Answer, Category


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author', 'creation_date']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author', 'creation_date']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# EOF