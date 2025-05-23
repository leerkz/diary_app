from django.forms import ModelForm
from diary.models import DiaryEntry
from django import forms

class DiaryEntryForm(ModelForm):
    class Meta:
        model = DiaryEntry
        exclude = ['user']



class DiaryEntrySearchForm(forms.Form):
    query = forms.CharField(
        label='Поиск',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Поиск'})
    )