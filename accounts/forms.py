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
            'charity_operating_continent' 
        )

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
            'charity_operating_continent' 
        )

class EditCustomUserProfileForm(forms.Form):
    charity_name = forms.CharField(max_length=255)
    charity_address_line_1 = forms.CharField(max_length=500)
    charity_address_line_2 = forms.CharField(max_length=500)
    charity_postcode = forms.CharField(max_length=50)
    charity_website_url = forms.URLField(help_text="Please enter a full URL starting with 'http://www...")
    charity_bio = forms.CharField (widget=forms.Textarea, max_length=2000)
    charity_country = CountryField().formfield()
    
    CONTINENT = (
        ('oc', 'We operate mainly in the country the charity is based.'),
        ('af', 'Africa'),
        ('as', 'Asia'),
        ('au', 'Australia/ Oceania'),
        ('eu', 'Europe'),
        ('na', 'North America'),
        ('sa', 'South America'),
    )

    charity_operating_continent = forms.ChoiceField(choices = CONTINENT)