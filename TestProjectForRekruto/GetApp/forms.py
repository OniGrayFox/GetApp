from django import forms

class GetAppForm(forms.Form):
    name = forms.CharField(max_length=180)
    surname = forms.CharField(max_length=180)

