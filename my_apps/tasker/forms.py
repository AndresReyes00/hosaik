from django import forms

from my_apps.tasker.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "priority",
            "due_date",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "What needs to be done?",
                    "autocomplete": "off",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add some details...",
                    "rows": 4,
                }
            ),
            "priority": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "due_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
                format="%Y-%m-%dT%H:%M",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["due_date"].input_formats = [
            "%Y-%m-%dT%H:%M",
        ]
