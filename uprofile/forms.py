from . models import Profile
from django import forms

class ProfileForm(forms.ModelForm):



    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'address', 'phone', 'profile_image',)


