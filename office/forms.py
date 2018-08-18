from django import forms
from django.contrib.auth.models import User


class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=20)
    repeat_password = forms.CharField(widget=forms.PasswordInput, label='Repeat Password', max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password', 'repeat_password']

    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError("Passwords don't match")
