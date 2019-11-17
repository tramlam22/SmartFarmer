from django import forms
from webapp.models import Account

class createAccountForm(forms.ModelForm):
    firstName = forms.CharField(label="First Name:",max_length=45)
    lastName = forms.CharField(label="Last Name:",max_length=45)
    username = forms.CharField(label="Username:",max_length=45)
    password = forms.CharField(label="Password:",max_length=45)

    class Meta:
        model = Account
        fields = ('username','password')