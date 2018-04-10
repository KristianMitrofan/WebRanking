from django import forms

class NameForm(forms.Form):
    first_player = forms.CharField(label='first_player', max_length=100)
    second_player = forms.CharField(label='second_player', max_length=100)