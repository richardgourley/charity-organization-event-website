from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django_countries.fields import CountryField

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 
            'email', 
            'charity_name',
            'charity_address_line_1', 
            'charity_address_line_2',
            'charity_postcode',
            'charity_website_url',
            'charity_bio',
            'charity_country',
            'charity_operating_continent',
            'charity_image',
        )

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control mb-4 border'}),
            'email':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_name':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_address_line_1':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_address_line_2':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_postcode':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_website_url':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_bio':forms.Textarea(attrs={'class':'form-control  mb-4'}),
            'charity_country':forms.Select(attrs={'class':'form-control form-select mb-4'}),
            'charity_operating_continent':forms.Select(attrs={'class':'form-control form-select mb-4'}),
            'charity_image':forms.FileInput(attrs={'class':'form-control mb-4'}),
            
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 
            'email', 
            'charity_name',
            'charity_address_line_1', 
            'charity_address_line_2',
            'charity_postcode',
            'charity_website_url',
            'charity_bio',
            'charity_country',
            'charity_operating_continent',
            'charity_image',
        )

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control mb-4 border'}),
            'email':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_name':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_address_line_1':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_address_line_2':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_postcode':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_website_url':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_bio':forms.Textarea(attrs={'class':'form-control  mb-4'}),
            'charity_country':forms.Select(attrs={'class':'form-control form-select mb-4'}),
            'charity_operating_continent':forms.Select(attrs={'class':'form-control form-select mb-4'}),
            'charity_image':forms.FileInput(attrs={'class':'form-control mb-4'}),
            
        }

class EditCustomUserProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "charity_name",
            "charity_address_line_1",
            "charity_address_line_2",
            "charity_postcode",
            "charity_website_url",
            "charity_bio",
            "charity_country",
            "charity_operating_continent",
            "charity_image"
        )

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control mb-4 border'}),
            'email':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_name':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_address_line_1':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_address_line_2':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_postcode':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_website_url':forms.TextInput(attrs={'class':'form-control mb-4'}),
            'charity_bio':forms.Textarea(attrs={'class':'form-control  mb-4'}),
            'charity_country':forms.Select(attrs={'class':'form-control form-select mb-4'}),
            'charity_operating_continent':forms.Select(attrs={'class':'form-control form-select mb-4'}),
        }
