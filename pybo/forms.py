from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'file']

        labels = {
            'subject': 'Subject',
            'content': 'Content',
            'file': 'File',
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': 'Content',
        }
