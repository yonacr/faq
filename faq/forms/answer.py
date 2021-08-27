from django import forms
from faq.models import Answer


class AnswerCreateForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = "Réponse"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# EOF
