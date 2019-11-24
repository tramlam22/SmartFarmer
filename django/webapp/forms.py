from django import forms
from webapp.models import Account

class loginForm(forms.Form):
    username = forms.CharField(label="Username:",max_length=45, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label="Password:",max_length=45, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class createAccountForm(forms.ModelForm):
    firstName = forms.CharField(label="First Name:",max_length=45, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    lastName = forms.CharField(label="Last Name:",max_length=45, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    username = forms.CharField(label="Username:",max_length=45, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password:",max_length=45, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = Account
        fields = ('username','password')