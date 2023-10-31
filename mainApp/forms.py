
from django import forms
from .models import Question,Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, user, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super(QuestionForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
        widgets = {
            'answer_text': forms.Textarea(attrs={'rows': 4}),
        }