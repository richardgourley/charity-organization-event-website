from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

class CustomUser(AbstractUser):
    charity_name = models.CharField(max_length=255)
    charity_address_line_1 = models.CharField(max_length=500)
    charity_address_line_2 = models.CharField(max_length=500)
    charity_postcode = models.CharField(max_length=50)
    charity_website_url = models.URLField(help_text="Please enter a full URL ensurint it starts with 'http://www...")
    charity_bio = models.TextField(max_length=2000)

    charity_country = CountryField()

    CONTINENT = (
        ('oc', 'We operate mainly in the country the charity is based.'),
        ('af', 'Africa'),
        ('as', 'Asia'),
        ('au', 'Australia/ Oceania'),
        ('eu', 'Europe'),
        ('na', 'North America'),
        ('sa', 'South America'),
    )

    charity_operating_continent = models.CharField(
        max_length=2,
        choices=CONTINENT,
        default='oc',
        help_text='Which continent of the world do you mainly operate in? (Alternatively, select "We operate mainly in the country the charity is based.")'
    )

    def __str__(self):
        return self.username
