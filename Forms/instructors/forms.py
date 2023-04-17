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
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if len(name) < 4:
            raise ValidationError('The name should be greater than 4 characters')
        if '@' not in email:
            raise ValidationError('Email must have `@` symbol in it.')

        def password_length():
            if len(password) < 8:
                raise ValidationError('Password must be greater than 8!') 

        def upper_case():
            if not any(char.isupper() for char in password):
                raise ValidationError('Password must contain atleast on uppercase.')

        def lower_case():
            if not any(char.islower() for char in password):
                raise ValidationError('Password must contain atleast on lowercase.')
        
        def check_number():
            if not any(char.isdigit() for char in password):
                raise ValidationError('Password must contain atleast on digit.')

        def has_special_character(password):
            special_characters = ['@', '#', '$', '&']
            for char in password:
                if char in special_characters:
                    return True
            raise ValidationError('Password must have `@`, `#`, `$`, `%`')

        # Password Validation
        password_length()       
        upper_case()
        lower_case()
        check_number()
        has_special_character(password)
        