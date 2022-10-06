from dataclasses import field
from django import forms
from .models import Either

class EitherForm(forms.ModelForm):
    class Meta:
        model = Either
        fields = '__all__'