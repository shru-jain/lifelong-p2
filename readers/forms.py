# forms.py
from django import forms
from .models import Book, User

class OptionsForm(forms.Form):
    options = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=''
    )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'price']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'liked_books']
        widgets = {
            'liked_books': forms.CheckboxSelectMultiple
        }