
from django import forms
from django.contrib.auth.hashers import check_password

from .models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=50)
    password = forms.CharField(label='Password',
                               max_length=50,
                               widget=forms.PasswordInput)
    email = forms.CharField(label='E-mail', required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        if user:
            raise forms.ValidationError('El nombre de usuario ya existe')

    def clean_email(self):
        email = self.cleaned_data['email']
        email = User.objects.filter(email=email)
        if len(email) == 0:
            return email
        else:
            raise forms.ValidationError('La direccion de email ya existe')

class SiginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=50)
    password = forms.CharField(label='Password',
                               max_length=50,
                               widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = self.cleaned_data
        from .models import User

        try:
            user = User.objects.get(username=self.cleaned_data.get('username'))
        except User.DoesNotExist:
            raise forms.ValidationError('Datos incorrectos')
        if not check_password(self.cleaned_data.get('password'), user.password):
            raise forms.ValidationError('Datos incorrectos')
        return cleaned_data

