from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    message = forms.CharField(label="Your message", max_length=100)