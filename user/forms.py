from datetime import datetime
from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'id_profile_image'}), label='Profile Image',required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','title':"Please use a 10 digit mobile number", 'pattern':"[1-9]{1}[0-9]{9}"}),required=True)
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','cols':"4",'rows':'3'}),required=False)
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}),
        min_length=8, validators=[RegexValidator('^(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+*!=]).*$', message="At Least One Uppercase Character,One Lowercase Character,One Numeric Value And One Special Character(!@#$%^&*) Required ")],
    )
    class Meta:
        model = UserProfile
        fields = ('profile_image','name','username','phone_no', 'email','comments','password')
    
  
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
