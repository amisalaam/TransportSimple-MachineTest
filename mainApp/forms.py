
from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

    def __init__(self, user, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super(QuestionForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
