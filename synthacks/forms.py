from django import forms
from .models import Team


class Form(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    second_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    third_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = Team
        fields = ('first_name','second_name','third_name')