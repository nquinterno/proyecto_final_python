from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *


class UserViewForm(forms.ModelForm):
    username = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        super(UserViewForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput, help_text='')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class ProfileCreationForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    web = forms.URLField()

    class Meta:
        model = Profile
        fields = ['nombre', 'apellido', 'descripcion', 'web']

class ProfileDisplayForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['nombre', 'apellido', 'descripcion', 'web']

    def __init__(self, *args, **kwargs):
        super(ProfileDisplayForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

class FormAvatar(forms.ModelForm):
    imagen = forms.ImageField()
    class Meta:
        model = Avatar
        fields = ['imagen']
    
    