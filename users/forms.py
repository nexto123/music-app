from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import UserProfile
from django.forms import ModelForm, Textarea, CharField, ImageField, FileField,FileInput
from django_countries.widgets import CountrySelectWidget





class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class UserProForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('image','display_name','website', 'phone', 'country', 'county','description')

        widgets = {
            'image': forms.FileInput(attrs={'class': 'Image-input-field btn btn-secondary bg-white form-control-file text-black'}),
            'display_name': forms.TextInput(attrs={'class': 'display-input-field'}),
            'description': forms.Textarea(attrs={'class': 'description-input'}),
            'website': forms.TextInput(attrs={'class': 'web-input'}),
            'phone': forms.TextInput(attrs={'class': 'phone-c'}),
            'country': CountrySelectWidget(attrs={'class': 'country-c'}),
            'county': forms.TextInput(attrs={'class': 'county-c'}),
            'created_date': forms.TextInput(attrs={'class': 'created-c'}),

        }

        labels = {
            "image": "Profile Pic"
        }

