# forms.py
from django import forms
from .models import Book

class OptionsForm(forms.Form):
    options = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'price']