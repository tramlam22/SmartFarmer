from django import forms
from webapp.models import AuthUser
from webapp.models import dataMCU

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

class createDataForm(forms.ModelForm):

    # Note to tram: I didn't realize that the soil sensor also did soil temp. Could you add 
    # that to the database or is it too late?

    # Also, I have no idea what im doing and I think you have a better idea than I do.
    # Why are names from forms.py slightly different from models.py ah im lost

    # I think this is where the data gets processed and validated?

    #data string 
    #num=1&temp=23.700&hum=41.000&soil_t=-1.000&soil=65535
    #missing batterylvl and 

    # -- Justin 


    class Meta:
        model = dataMCU
        fields = ['mcu_no','temperature', 'humidity', 'soil_moisture', 'soil_temp', 'light_reading', 'heat_index', 'battery_level']

    mcu_no = forms.CharField(

    )
    temperature = forms.CharField(
        label='temp'
    )