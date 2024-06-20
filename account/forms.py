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



    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'