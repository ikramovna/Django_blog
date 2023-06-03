from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import (Form, CharField, EmailField, PasswordInput, ModelForm)

from apps.users.models import UserProfile


class RegistrationForm(Form):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    username = CharField(max_length=30)
    email = EmailField()
    password1 = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Confirm Password', widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is already in use.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match.')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class LoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio',)
