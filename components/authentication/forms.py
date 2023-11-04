from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from domain.entities.authentication.userEntity import user
class institutionForm (UserCreationForm):
    institutionCode = forms.CharField(max_length=100, required=True, help_text="Write your institution code")
    description = forms.CharField(max_length=200, required=True, help_text="Write a short text about your institution (less than 200 words)")
    class Meta:
        model = user
        fields = ('username', 'email','password1', 'password2','institutionCode','description')