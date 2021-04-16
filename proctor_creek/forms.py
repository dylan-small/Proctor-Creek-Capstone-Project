from django import forms

class Report(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    summary = forms.CharField(max_length=30)