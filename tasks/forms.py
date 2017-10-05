from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.Textarea()
    due_date = forms.DateTimeField()