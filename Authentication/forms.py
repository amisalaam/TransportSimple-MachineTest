from django import forms
from .models import Account


class RegistrationalForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'form-control',
    }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirm Password',
       
    }
    ))
    class Meta:
        model = Account
        fields = ['full_name','email','password']


    
    def __init__(self, *args, **kwargs):
        super(RegistrationalForm, self).__init__(*args, **kwargs)
        
        self.fields['full_name'].widget.attrs['placeholder'] = 'Enter Full Name'
        
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



    def clean(self):
        cleaned_data = super(RegistrationalForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'password does not match!'
            )


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Email',
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))