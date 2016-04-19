from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email',]
    
    #  my custom validation for the field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extention = provider.split(".")
        if not extention == "edu":
            raise forms.ValidationError("Please enter valid .edu email address")
        return email
    
    #  my custom validation for the field
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # custom validation code
        return full_name


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

















    
    