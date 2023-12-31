from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from domain.entities.authentication.userEntity import user
class institutionForm (UserCreationForm):
    """
    A form for recording data about an institution.

    This form is used to collect information about an institution,
    including its username, email address, password, institution code and a brief description,
    institution code, and a brief description.

    Attributes
    ----------

    - institutionCode: str
         A text field to enter the institution code.
    - description: str
        A text field to enter a short description of the institution.

        
    Fields inherited from UserCreationForm
    --------------------------------------
    - username: str 
        The username of the institution.
    - email: str
        The institution's email address.
    - password1: str
        The institution's password.
    - password2: str
        Confirmation of the password.

    Args
    -----
    - *args: Additional positional arguments.
    - kwargs: Additional keyword arguments.

    Methods
    --------
    - __init__(*args,**kwargs): 
        - Constructor that customizes the attributes of the username, email and password fields.
        - User name, email and password fields with placeholders.

    Note: This class extends UserCreationForm (Django authentications form) and adds institution-specific fields.

    """
    institutionCode = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your institution code'}))
    description = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'About your institution'}))
    class Meta:
        model = user
        fields = ('username', 'email','password1', 'password2','institutionCode','description')
    def __init__(self, *args, **kwargs):
        super(institutionForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Your institution name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'


class studentForm (UserCreationForm):
    """
    A form for recording data about a student.

    This form is used to collect information about a student,
    including its username, email address, password, age, interest and skills. 

    Attributes
    ----------

    - age: int
        An integer field to enter the age of the student.
    - interest: str
        A text field to enter interests of the student.
    - skills: str
        A text field to enter skills that the student currently have.

        
    Fields inherited from UserCreationForm
    --------------------------------------
    - username: str 
        The username of the student.
    - email: str
        The student's email address.
    - password1: str
        The student's password.
    - password2: str
        Confirmation of the password.

    Args
    -----
    - *args: Additional positional arguments.
    - kwargs: Additional keyword arguments.

    Methods
    --------
    - __init__(*args,**kwargs): 
        - Constructor that customizes the attributes of the username, email and password fields.
        - User name, email and password fields with placeholders.

    Note: This class extends UserCreationForm (Django authentications form) and adds student-specific fields.

    """
    age = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your age'}))
    interest = forms.CharField(max_length=45, required=True, widget=forms.TextInput(attrs={'placeholder': 'Topic of your interest'}))
    skills = forms.CharField(max_length=45, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your skills'}))
    class Meta:
        model = user
        fields = ('username', 'email','password1', 'password2','age','interest','skills')
    def __init__(self, *args, **kwargs):
        super(studentForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Your student name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'