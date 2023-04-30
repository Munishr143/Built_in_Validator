from django import forms

from django.core import validators
from app.models import *

class Student(forms.Form):
    name=forms.CharField(max_length=30, validators=[validators.MaxLengthValidator(6)])
    age=forms.IntegerField(validators=[validators.MinValueValidator(18)])
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

class Topic_Form(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
