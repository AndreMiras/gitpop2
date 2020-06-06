from urllib.error import URLError
from urllib.request import urlopen
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
            content = urlopen(data)
        except URLError as e:
            raise forms.ValidationError("The provided GitHub URL does not exist.")
        return data

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        """
        Adds Twitter Bootstrap 3 "form-control" class.
        """
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
