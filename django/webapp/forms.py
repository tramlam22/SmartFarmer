from django import forms
from webapp.models import AuthUser

class loginForm(forms.Form):
    username = forms.CharField(label="Username:",max_length=45, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label="Password:",max_length=45, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class createAccountForm(forms.ModelForm):
    firstName = forms.CharField(
        required = 'True',
        label="First Name:",
        max_length=45, 
        widget=forms.TextInput(attrs={'placeholder': 'First name', 'autocomplete': 'off'})
    )
    lastName = forms.CharField(
        required = 'True',
        label="Last Name:",
        max_length=45, 
        widget=forms.TextInput(attrs={'placeholder': 'Last name', 'autocomplete': 'off'})
    )
    email = forms.CharField(
        required = 'True',
        label="E-mail:",
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'hello@example.com'})
    )
    username = forms.CharField(
        required = 'True',
        label="Username:",max_length=45, 
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'autocomplete': 'off'})
    )
    password = forms.CharField(
        required = 'True',
        label="Password:",
        max_length=45, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'autocomplete': 'new-password'})
    )

    class Meta:
        model = AuthUser
        fields = ('username','password','email','firstName','lastName')
