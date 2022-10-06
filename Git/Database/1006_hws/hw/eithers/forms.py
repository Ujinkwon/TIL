from dataclasses import field, fields
from django import forms
from .models import Either, Comment

class EitherForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='title',
    #     widget=forms.Textarea(
    #         attrs={
    #             'style': 'width: 10%;'
    #         }
    #     )
    # )
    class Meta:
        model = Either
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('either', )