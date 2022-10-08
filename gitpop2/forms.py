from urllib.error import URLError
from urllib.request import urlopen

from django import forms


class PopForm(forms.Form):
    giturl = forms.URLField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "https://github.com/django/django",
                "class": "form-control",
            }
        )
    )

    def clean_giturl(self):
        data = self.cleaned_data["giturl"]
        try:
            urlopen(data)
        except URLError:
            raise forms.ValidationError(
                "The provided GitHub URL does not exist."
            )
        return data
