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

class EditCustomUserProfileForm(forms.Form):
    charity_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-4'}), max_length=255)
    charity_address_line_1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-4'}), max_length=500)
    charity_address_line_2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-4'}), max_length=500)
    charity_postcode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-4'}), max_length=50)
    charity_website_url = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control mb-4'}), help_text="Please enter a full URL starting with 'http://www...")
    charity_bio = forms.CharField (widget=forms.Textarea(attrs={'class':'form-control  mb-4'}), max_length=2000)
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

    charity_operating_continent = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control form-select mb-4'}), choices = CONTINENT)
    charity_image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control mb-4'}))