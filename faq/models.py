from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(
        max_length=256
    )


class Answer(models.Model):

    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    creation_date = models.DateTimeField(
        auto_now_add=True
    )


class Question(models.Model):

    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    creation_date = models.DateTimeField(
        auto_now_add=True
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.SET_NULL,
        null=True
    )

# EOF
