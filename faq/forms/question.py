from django import forms

from faq.models import Question


class QuestionUpdateForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].label = "Catégorie de la question"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class QuestionCreateForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Ecrivez votre question ici"
            }
        )

# EOF
