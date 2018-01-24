from django import forms
from django.contrib.auth import forms as auth_forms
from captcha.fields import ReCaptchaField


class SubmissionForm(forms.Form):
    answer = forms.CharField(required=True, label='Answer')


class LoginWithCaptcha(auth_forms.AuthenticationForm):
    captcha = ReCaptchaField()
