from django import forms
from django.forms import ValidationError


class Instructor(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        strip=True
    )

# Adding Validation for all fields 
    def clean(self):
        cleaned_data =  super().clean()
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if len(name) < 4:
            raise ValidationError('The name should be greater than 4 characters')
        if '@' not in email:
            raise ValidationError('Email must have `@` symbol in it.')
        
        # Password Validation

        if not any(char.isupper() for char in password):
            raise ValidationError('Password must contain atleast on uppercase.')
        if not any(char.islower() for char in password):
            raise ValidationError('Password must contain atleast on lowercase.')
        if not any(char.digit() for char in password):
            raise ValidationError('Password must contain atleast on digit.')
        