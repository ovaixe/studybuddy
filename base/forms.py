from typing import Any
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Room, UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    ),
                    'placeholder': 'Enter your First Name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    ),
                    'placeholder': 'Enter your Last Name'
                }),
            'username': forms.TextInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    ),
                    'placeholder': 'Enter your username'
                }),
            'email': forms.EmailInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    ),
                    'placeholder': 'Enter your email'
                }),
        }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': (
                'w-full text-slate-300 rounded-lg bg-slate-800 '
                'py-2 px-3 focus:outline-none'
            ),
            'placeholder': 'Enter your password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': (
                'w-full text-slate-300 rounded-lg bg-slate-800 '
                'py-2 px-3 focus:outline-none'
            ),
            'placeholder': 'Confirm your password'
        })

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    )
                }),
            'first_name': forms.TextInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    )
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    )
                }),
            'email': forms.TextInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    )
                }),
        }


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']
        widgets = {
            'bio': forms.Textarea(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    )
                }),
            'avatar': forms.FileInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    )
                }),
        }


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        widgets = {
            'topic': forms.Select(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    )
                }),
            'name': forms.TextInput(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    )
                }),
            'description': forms.Textarea(
                attrs={
                    'class': (
                        'w-full text-slate-300 rounded-lg bg-slate-800 '
                        'py-2 px-3 focus:outline-none'
                    )
                }),
        }
