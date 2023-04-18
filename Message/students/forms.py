from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput,
        label= 'Password',
        initial=None
    )
    class Meta:
        model = Student
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')


        if len(name) < 4:
            raise ValidationError('Name must be greater than 4')
        

        if '@' not in email:
            raise ValidationError('Email must have @ symbol')
        
        if len(password) < 8:
            raise ValidationError('Password must have 8 characters')
        
            