from django.test import TestCase
from datetime import datetime
#from .models import Event
from accounts.models import CustomUser

class CustomUserModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Create Custom User
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
            charity_image="test_user_image.jpg"
        )

    def test_custom_user_details_saved_correctly(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        self.assertEqual(custom_user.username, "test_user_1")
        self.assertEqual(custom_user.email, "email@test_charity.com")
        self.assertEqual(custom_user.charity_name, "Test Charity")
        self.assertEqual(custom_user.charity_bio, "A test charity number 1")

    def test_charity_name_verbose_name(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        verbose_name = custom_user._meta.get_field('charity_name').verbose_name

    def test_charity_name_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_name').max_length
        self.assertEqual(max_length, 255)

    def test_charity_address_line_1_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_address_line_1').max_length
        self.assertEqual(max_length, 500)

    def test_charity_address_line_2_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_address_line_2').max_length
        self.assertEqual(max_length, 500)

    def test_charity_postcode_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_postcode').max_length
        self.assertEqual(max_length, 50)

    def test_charity_website_url_help_text(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        help_text = custom_user._meta.get_field('charity_website_url').help_text
        self.assertEqual(help_text, "Please enter a full URL starting with 'http://www...'")

    def test_charity_bio_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_bio').max_length
        self.assertEqual(max_length, 2000)

    def test_charity_bio_help_text(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        help_text = custom_user._meta.get_field('charity_bio').help_text
        self.assertEqual(help_text, 'Add a short description as to what your charity does and who it benefits.')

    def test_charity_country_field_name(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        country_name = custom_user.charity_country.country_name
        self.assertEqual(country_name, 'Australia')

    def test_charity_operating_continent_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_operating_continent').max_length
        self.assertEqual(max_length, 2)

    def test_charity_operating_continent_choices_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        length = len(custom_user._meta.get_field('charity_operating_continent').choices)
        self.assertEqual(length, 7)

    def test_charity_operating_continent_default(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        default = custom_user._meta.get_field('charity_operating_continent').default
        self.assertEqual(default, 'oc')

    def test_charity_operating_continent_help_text(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        help_text = custom_user._meta.get_field('charity_operating_continent').help_text
        self.assertEqual(help_text, 'Which continent of the world do you mainly operate in? (Alternatively, select "We operate mainly in the country the charity is based.")')

    def test_charity_image_upload_to(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        upload_to = custom_user._meta.get_field('charity_image').upload_to
        self.assertEqual(upload_to, 'charities')

    def test_charity_image_field_null_is_true(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        is_null = custom_user._meta.get_field('charity_image').null
        self.assertEqual(is_null, True)

    def test_charity_image_help_text(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        help_text = custom_user._meta.get_field('charity_image').help_text
        self.assertEqual(help_text, 'Upload a charity logo.')

    def test_approved_field_default(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        default = custom_user._meta.get_field('approved').default
        self.assertEqual(default, False)

    def test_custom_user_string_equal_to_custom_user_username(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        self.assertTrue(custom_user.__str__() == custom_user.username)

