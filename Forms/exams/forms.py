from django import forms
from django.core import validators
from django.forms import ValidationError


def exact_name(name):
    if name != 'Usman':
        raise ValidationError('Name should be Usman')

# FORMS WIDGETS EXAMPLE:
class StudentExam(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput,
        empty_value='Not Given',
        error_messages={
        'required': 'Enter Your Name'
        },
        validators=[exact_name] # custom validation used in built-in validators
    )
    # bio = forms.CharField(
    #     widget=forms.Textarea
    # )
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password',
        strip=True,
    )
    repassword = forms.CharField(
        widget=forms.PasswordInput,
        label='Again Password',
        strip=True,
    )
    # price = forms.DecimalField(
    #     min_value=5,
    #     max_value=100,
    #     max_digits=4,
    #     decimal_places=1,
    # )

    # adding Validation

    # def clean_name(self):
    #     validating_name = self.cleaned_data['name']
    #     if len(validating_name) < 4:
    #         raise forms.ValidationError('Enter more than or equal to 4 characters')
    #     return validating_name

    def clean(self):
        cleaned_data = super().clean()
        validate_password = self.cleaned_data['password']
        validate_repassword = self.cleaned_data['repassword']
        if validate_password != validate_repassword:
            raise ValidationError('Password not matched')
        



"""
NOTE: 
    There are many types of widgets, we can use it for different purposes, this is very benificial for us.
    - Form field types
    
"""