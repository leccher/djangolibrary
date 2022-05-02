from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddBookForm(forms.Form):
    title   = forms.CharField(help_text="Inserire il titolo.")
    subtitle = forms.CharField(help_text="Inserire l'ventuale sottotitoli.") 
    summary = forms.Textarea()
    isbn = forms.CharField(max_length=13)
    pages = forms.IntegerField()
    vendor_url = forms.URLField()
    coauthors = forms.CharField()
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    saga = forms.ModelChoiceField(queryset=Saga.objects.all())
    language = forms.ModelChoiceField(queryset=Language.objects.all())
    publisher = forms.ModelChoiceField(help_text="Scegliere l'editore",queryset=Publisher.objects.all())
    series = forms.ModelChoiceField(help_text="Scegliere la collana",queryset=Series.objects.all())
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())

class LoanForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    loaner = forms.ModelChoiceField(queryset=Loaner.objects.all())
    loan_date = forms.DateField()
    back_date = forms.DateField(required=False)

class LoanBackForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    loaner = forms.ModelChoiceField(queryset=Loaner.objects.all())
    loan_date = forms.DateField(required=True)
    #back_date = forms.DateField(required=False)
