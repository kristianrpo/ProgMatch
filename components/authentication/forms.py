from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from domain.entities.authentication.userEntity import user
class institutionForm (UserCreationForm):
    institutionCode = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your institution code'}))
    description = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'About your institution'}))
    class Meta:
        model = user
        fields = ('username', 'email','password1', 'password2','institutionCode','description')
    def __init__(self, *args, **kwargs):
        super(institutionForm, self).__init__(*args, **kwargs)

        # Personaliza los marcadores de posición para los campos heredados
        self.fields['username'].widget.attrs['placeholder'] = 'Your institution name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'