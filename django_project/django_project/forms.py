from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='ques', max_length=100)