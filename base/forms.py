from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Room


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'ml-5 rounded-lg bg-slate-700 py-1 px-2 focus:outline-none',
                'placeholder': 'Enter your username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'ml-5 rounded-lg bg-slate-700 py-1 px-2 focus:outline-none',
                'placeholder': 'Enter your password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'ml-5 rounded-lg bg-slate-700 py-1 px-2 focus:outline-none',
                'placeholder': 'Confirm your password'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'host': forms.Select(attrs={'class': 'ml-5 rounded-lg bg-slate-700 py-1 px-2 focus:outline-none'}),
            'topic': forms.Select(attrs={'class': 'ml-5 rounded-lg bg-slate-700 py-1 px-2 focus:outline-none'}),
            'name': forms.TextInput(attrs={'class': 'ml-5 rounded-lg bg-slate-700 py-1 px-2 focus:outline-none'}),
            'description': forms.Textarea(attrs={'class': 'ml-5 rounded-lg bg-slate-700 py-1 px-2 focus:outline-none'}),
            'participants': forms.Select(attrs={'class': 'ml-5 rounded-lg bg-slate-700 py-1 px-2 focus:outline-none', 'multiple': 'true'})
        }