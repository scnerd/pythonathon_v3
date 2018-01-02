from django import forms

class SubmissionForm(forms.Form):
    answer = forms.TextInput(label='Answer')