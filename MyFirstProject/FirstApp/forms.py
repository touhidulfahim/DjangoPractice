from django import forms

class user_form(forms.Form):
    user_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter valid username'}))
    user_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Please enter valid email'}))
    user_dob=forms.DateField(label='Birth Date', widget=forms.TextInput(attrs={'type':'date'}))
