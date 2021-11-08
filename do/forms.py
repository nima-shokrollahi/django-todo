from django import forms
from .models import Do


class AddDoForm(forms.ModelForm):
    class Meta:
        model = Do
        fields = ['title', 'description','date']


class AddDoFormOrj(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()
