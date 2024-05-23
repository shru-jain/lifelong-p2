# forms.py
from django import forms

class OptionsForm(forms.Form):
    options = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )