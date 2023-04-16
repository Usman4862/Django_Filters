from django import forms

# FORMS WIDGETS EXAMPLE:
class StudentExam(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput,
        empty_value='Not Given',
        error_messages={
        'required': 'Enter Your Name'
        }
    )
    bio = forms.CharField(
        widget=forms.Textarea
    )
    test = forms.CharField(
        widget=forms.PasswordInput,
        label='Password',
        strip=True,
    )
    email = forms.EmailField()
    price = forms.DecimalField(
        min_value=5,
        max_value=100,
        max_digits=4,
        decimal_places=1,
    )

    # adding Validation

    def clean_name(self):
        validating_name = self.cleaned_data['name']
        if len(validating_name) < 4:
            raise forms.ValidationError('Enter more than or equal to 4 characters')
        return validating_name




"""
NOTE: 
    There are many types of widgets, we can use it for different purposes, this is very benificial for us.
    - Form field types
    
"""