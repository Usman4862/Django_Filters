from django import forms


class StudentsRegistration(forms.Form):
    #NOTE:  Form Arguments
    name = forms.CharField(
        label='Your Name',
        label_suffix=' ',
        initial='usman malik',
        required=False,
        disabled=True,
        help_text=' '
    )
    email = forms.EmailField()
    age = forms.CharField()
    key = forms.CharField(widget=forms.HiddenInput()) # this is used for the hidden input fields.
