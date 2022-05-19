from unittest.util import _MAX_LENGTH
from django import forms

class TaskForm(forms.Form):
    desciption = forms.CharField(label='Task description', max_length=160)
    deadline = forms.DateField(label='Deadline')
    progress = forms.IntegerField(label='Progress', min=0, max = 100)

