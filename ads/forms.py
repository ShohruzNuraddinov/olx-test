from django import forms
from django.contrib.auth.forms import AuthenticationForm
# from snowpenguin.django.recaptcha2.fields import ReCaptchaField
# from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class CSVImortForm(forms.Form):
    csv_file = forms.FileField()


# class AuthForm(AuthenticationForm):
#     captcha = ReCaptchaField(widget=ReCaptchaWidget())
