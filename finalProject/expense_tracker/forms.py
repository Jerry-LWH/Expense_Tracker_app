# dappx/forms.py
from django import forms
from expense_tracker.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    """This class creates a form with the user's information."""
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField()
    first_name=forms.CharField()
    first_name=forms.CharField()

    class Meta():
        """This class creates a user with those information."""
        model = User
        fields = ('first_name','last_name','username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    """This class creates a form for viewing and updating the user's profile."""
    class Meta():
        """This class creates a user's profile with those information."""
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
