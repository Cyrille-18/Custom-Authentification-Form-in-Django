from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import authenticate

class MyAuthentificationForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = "Identifiant ou mot de passe incorrect."

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                self.add_error(None, forms.ValidationError(self.error_messages['invalid_login'], code='invalid_login'))
        return self.cleaned_data

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    newpassword = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        newpassword = cleaned_data.get("newpassword")
        confirmpassword = cleaned_data.get("confirmpassword")

        if newpassword != confirmpassword:
            self.add_error('confirmpassword', "Les mots de passe ne correspondent pas.")
        return cleaned_data