from django import forms
from django.contrib.auth import forms as auth_forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class SubmissionForm(forms.Form):
    answer = forms.CharField(required=True, label='Answer')


class LoginWithCaptcha(auth_forms.AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())


class UserCreationFormWithCaptcha(auth_forms.UserCreationForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())