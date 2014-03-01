from django import forms

class PopForm(forms.Form):
    # url = forms.CharField()
    giturl = forms.URLField(
        widget=forms.TextInput(attrs={
            'placeholder': 'https://github.com/django/django',
            'class': 'input-xlarge',
            }))
