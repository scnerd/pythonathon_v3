from django import forms

class SubmissionForm(forms.Form):
    answer = forms.CharField(required=True, label='Answer')