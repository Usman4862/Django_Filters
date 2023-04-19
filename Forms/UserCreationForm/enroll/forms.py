from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class Register(UserCreationForm):
    password2 = forms.CharField(
        label='Password (Again)',
        widget=forms.PasswordInput,
        strip=False,
        # label_suffix='---',
    )
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
        ]
        labels = {
            'username': 'User Name',
            'first_name': 'Very First Name',
            'last_name': 'Very Last Name',
            'email': 'Email (G-mail)'
        }


class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'User Name',
            'first_name': 'Very First Name',
            'last_name': 'Very Last Name',
            'email': 'Email (G-mail)'
        }