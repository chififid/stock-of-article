from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator



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



class ConfirmFormSix(forms.Form):
    units = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    tens = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    hundreds = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    thousands = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    tens_of_thousands = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    hundreds_of_thousands = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    units.widget.attrs.update({'min': '0', 'max': '9', 'class': 'key_form'})
    tens.widget.attrs.update({'min': '0', 'max': '9', 'class': 'key_form'})
    hundreds.widget.attrs.update({'min': '0', 'max': '9', 'class': 'key_form'})
    thousands.widget.attrs.update({'min': '0', 'max': '9', 'class': 'key_form'})
    tens_of_thousands.widget.attrs.update({'min': '0', 'max': '9', 'class': 'key_form'})
    hundreds_of_thousands.widget.attrs.update({'min': '0', 'max': '9', 'class': 'key_form'})
