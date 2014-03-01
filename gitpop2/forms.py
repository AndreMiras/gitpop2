from django import forms

class PopForm(forms.Form):
    # url = forms.CharField()
    giturl = forms.URLField()
