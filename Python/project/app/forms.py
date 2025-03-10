from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label="Title")
    description = forms.CharField(widget=forms.Textarea, required=False, label="Description")
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label="Due Date")
