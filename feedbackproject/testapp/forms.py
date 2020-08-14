from django import forms
from django.core import validators

def st(value):
    if value[0]!='v':
        raise forms.ValidationError('value must start with v')


class feed(forms.Form):
    name=forms.CharField(validators=[st])
    id=forms.IntegerField()
    mail=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])
