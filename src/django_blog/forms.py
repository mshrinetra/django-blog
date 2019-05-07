from django import forms


class ExampleForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
