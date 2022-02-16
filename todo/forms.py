from django import forms

class AddTaskForm(forms.Form):
    name = forms.CharField()
    notes = forms.CharField(widget=forms.Textarea)