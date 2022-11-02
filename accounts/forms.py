from django import forms
from . models import Account
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length = 60, help_text="Required. Add a valid email address.")
    class Meta:
        model = Account
        fields = ('username','email', )

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']