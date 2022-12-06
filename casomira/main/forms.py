from django import forms
from django.forms import CheckboxSelectMultiple
from models import Person



# class ZapisPersonForm(forms.Form):
#     choices = forms.ModelMultipleChoiceField(
#         queryset = Person.all()
#         widget = forms.CheckboxSelectMultiple
#     )

    # if request.method == "POST":
    #     form = ZapisPersonForm(request.POST):
    #     for id in form.cleaned_data['poeple']
