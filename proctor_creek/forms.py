from django import forms

class Report(forms.Form):
    first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=30)