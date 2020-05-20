from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


class MyForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'subjects', 'img', 'password1', 'password2')


class ConfirmForm(forms.Form):
    key = forms.IntegerField(label='key')
