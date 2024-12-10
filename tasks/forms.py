from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Task.objects.filter(title=title).exists():
            raise forms.ValidationError("Task with this title already exists.")
        return title
