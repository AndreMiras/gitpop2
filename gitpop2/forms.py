import urllib2
from django import forms

class PopForm(forms.Form):
    giturl = forms.URLField(
        widget=forms.TextInput(attrs={
            'placeholder': 'https://github.com/django/django',
            'class': 'input-xlarge',
            }))

    def clean_giturl(self):
        data = self.cleaned_data['giturl']
        try:
            content = urllib2.urlopen(data)
        except urllib2.URLError as e:
            raise forms.ValidationError("The provided GitHub URL does not exist.")
        return data
