from django import forms
from django.utils import timezone

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model =  Task
        fields = [
            "title",
            "description",
            "deadline",
            "is_complited",
            "created_at",

        ]

        def clean_dead(self):
            deadline = self.cleaned_data["deadline"]
            today = timezone.now().date()

            if deadline < today:
                raise forms.ValidationError("The deadline date can't be before today")
            
            return deadline