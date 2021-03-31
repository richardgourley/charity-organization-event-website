from django.test import TestCase
from .models import Event
from accounts.models import CustomUser
from django.urls import reverse

class SignUpViewTests(TestCase):
    @classmethod
    def setupTestData(cls):
        #Create Approved Custom User
        CustomUser.objects.create(
            username="test_user_1",
            email="email@testcharity.com",
            password='test_user_1',
            charity_name="Test Charity",
            charity_address_line_1="Main Road",
            charity_address_line_2="London",
            charity_postcode="LON234",
            charity_website_url="http://www.testcharity.com",
            charity_bio="A test charity number 1",
            charity_country='AU',
            charity_operating_continent="oc",
            charity_image="test_user_image.jpg",
            approved=True
        )

    def test_signup_view_exists_at_correct_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_view_accessible_by_url_name(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

class EditCustomUserProfileTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Create Approved Custom User
        CustomUser.objects.create(
            username="test_user_1",
            email="email@testcharity.com",
            password='test_user_1',
            charity_name="Test Charity",
            charity_address_line_1="Main Road",
            charity_address_line_2="London",
            charity_postcode="LON234",
            charity_website_url="http://www.testcharity.com",
            charity_bio="A test charity number 1",
            charity_country='AU',
            charity_operating_continent="oc",
            charity_image="test_user_image.jpg",
            approved=True
        )

    def test_url_redirects_if_not_logged_in(self):
        response = self.client.get('/accounts/editprofile/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/accounts/editprofile/')