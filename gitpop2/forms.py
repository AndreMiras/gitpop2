import urllib2
from django import forms

class PopForm(forms.Form):
    giturl = forms.URLField(
        widget=forms.TextInput(attrs={
            'placeholder': 'https://github.com/django/django',
            'class': 'form-control',
            }))

    def clean_giturl(self):
        data = self.cleaned_data['giturl']
        try:
            content = urllib2.urlopen(data)
        except urllib2.URLError as e:
            raise forms.ValidationError("The provided GitHub URL does not exist.")
        return data

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'input-xlarge',
            }))
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
