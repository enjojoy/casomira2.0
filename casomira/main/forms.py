from django import forms


class PristalForm(forms.Form):
    landing  = forms.TimeField()