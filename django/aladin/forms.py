from django import forms

class Aladin(forms.Form):
    urlOfPic = forms.CharField(label='URL field', max_length=300)
