from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Inheriting from the usercreation form and updating more info inside
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required="True")

    #Class to keep configurations in what place
    class Meta:
        # saves to the user model, and order of fields in the form
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# #LC A MODEL FORM which allows us create a form that works with a specific database model, in this case "User"
# inherits from form.ModelForm, i.e from the form of the model (model = User)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    #Class to keep configurations in what place
    class Meta:
        # saves to the user model, and order of fields in the form
        model = User
        fields = ['username', 'email']


# For profile picture updating, that is in our Profile model (Imported above)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]