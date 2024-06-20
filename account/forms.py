from django import forms
from account.models import Account


class RegistrationForm(forms.ModelForm):

    set_password = forms.CharField(label='Set Password', 
        widget=forms.PasswordInput(attrs={
            'placeholder':'Enter password',
            'class':'form-control'
        })
    )

    confirm_password = forms.CharField(
        label='Confirm Password(again)',
        widget=forms.PasswordInput(attrs={
            'placeholder':'Enter password',
            'class':'form-control'
        })
    )

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        labels = {
            'phone_number':'Phone',
            'first_name': 'First Name',
            'last_name': 'Last Name' 
        }


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.label_suffix = '' # I not use default label suffix

        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'