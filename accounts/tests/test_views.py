from django.test import TestCase
from datetime import datetime
from django.utils import timezone
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

    def test_signup_view_accessible_by_reverse_url(self):
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

    def test_reverse_url_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('accounts:editprofile'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/accounts/editprofile/')

    def test_logged_in_user_returns_200(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('accounts:editprofile'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('accounts:editprofile'))
        self.assertTemplateUsed(response, 'accounts/edit_custom_user_profile.html')

    def test_logged_in_user_details_appear_in_form(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('accounts:editprofile'))
        # Test address details appear as form values
        self.assertTrue('value="Test Charity"' in str(response.content))
        self.assertTrue('value="Main Road"' in str(response.content))
        self.assertTrue('value="London"' in str(response.content))
        self.assertTrue('value="LON234"' in str(response.content))
        self.assertTrue('value="http://www.testcharity.com"' in str(response.content))
        self.assertTrue('test_user_image.jpg' in str(response.content))

class AccountProfileViewTests(TestCase):
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

        #Create Staff Member - is_staff = True, approved = False (default)
        CustomUser.objects.create(
            username="staff_member",
            email="staff_member@testcharity.com",
            password='staff_member',
            charity_name="None",
            charity_address_line_1="None",
            charity_address_line_2="None",
            charity_postcode="None",
            charity_website_url="http://www.charityorganizationsass.com",
            charity_bio="None",
            charity_country='AU',
            charity_operating_continent="oc",
            charity_image="test_user_image.jpg",
            is_staff=True
        )

        # Create an approved event for the approved user - test_user_1
        #### NOTE - Unapproved events and events with dates in past are tested in 'Events'

        # Get test_user_1
        test_user_1 = CustomUser.objects.get(username="test_user_1")

        Event.objects.create(
                user=test_user_1,
                event_name='Approved event',
                event_description='A lovely event.',
                event_date=timezone.now() + datetime.timedelta(days=10),
                event_url='http://www.testevent.com/approved_event',
                approved=True,
                image='image1.jpg',
                slug='88_test_charity_approved_event'
            )

    def test_url_redirects_if_not_logged_in(self):
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/accounts/profile/')

    def test_reverse_url_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/accounts/profile/')
    
    # Expecting staff members to be redirected - profile pages are for charity owners
    def test_logged_in_staff_member_redirects(self):
        login self.client.login(username='staff_member', password='staff_member')
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_returns_200(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('accounts:profile'))
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_logged_in_user_details_appear_in_content(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('accounts:profile'))
        self.assertTrue('test_user_1' in str(response.content))
        self.assertTrue('Test Charity' in str(response.content))
        self.assertTrue('Main Road' in str(response.content))
        self.assertTrue('London' in str(response.content))
        self.assertTrue('http://www.testcharity.com' in str(response.content))
        self.assertTrue('A test charity number 1' in str(response.content))
        self.assertTrue('Australia' in str(response.content))
        self.assertTrue('We operate mainly in the country the charity is based.' in str(response.content))

    def test_event_name_and_description_appears_in_content(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('accounts:profile'))
        self.assertTrue('Approved event' in str(response.content))
        self.assertTrue('A lovely event.' in str(response.content))

    # Test the event created by test_user_1 appears in 'event' context variable
    def test_logged_in_user_event_appears_in_events_context(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('accounts:profile'))
        event = Event.objects.get(slug='88_test_charity_approved_event')
        self.assertTrue(event in response.context['events'])

    # Test 'num_events' is 1 in profile page context
    def test_logged_in_user_correct_num_events_in_context(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.context['num_events'], '1')

class CharityListViewTests(TestCase):
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

        # Create Unapproved Custom User
        # Approved = FALSE by default
        CustomUser.objects.create(
            username="test_user_2",
            email="email@testcharity.com",
            password='test_user_2',
            charity_name="Test Charity 2",
            charity_address_line_1="Main Road",
            charity_address_line_2="Edinburgh",
            charity_postcode="LON234",
            charity_website_url="http://www.testcharity2.com",
            charity_bio="A test charity number 2",
            charity_country='AU',
            charity_operating_continent="oc",
            charity_image="test_user_image.jpg"
        )

        #Create Staff Member - is_staff = True, approved = False (default)
        CustomUser.objects.create(
            username="staff_member",
            email="staff_member@testcharity.com",
            password='staff_member',
            charity_name="None",
            charity_address_line_1="None",
            charity_address_line_2="None",
            charity_postcode="None",
            charity_website_url="http://www.charityorganizationsass.com",
            charity_bio="None",
            charity_country='AU',
            charity_operating_continent="oc",
            charity_image="test_user_image.jpg",
            is_staff=True
        )

    def test_exists_at_correct_url(self):
        response = self.client.get('/all_charities/')
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(reverse('all_charities'))
        self.assertTemplateUsed(response, 'accounts/charity_list.html')

    def test_accessible_by_url_name(self):
        response = self.client.get(reverse('all_charities'))
        self.assertEqual(response.status_code, 200)

    def test_number_of_users_in_context_is_1(self):
        response = self.client.get(reverse('all_charities'))
        self.assertEqual(len(response.context['users']), 1)

    def test_approved_member_in_context(self):
        response = self.client.get(reverse('all_charities'))
        self.assertEqual(response.status_code, 200)
        test_user_1 = CustomUser.objects.get(username='test_user_1')
        self.assertTrue(test_user_1 in response.context['users'])

    # Test that unapproved custom user does not appear in 'users' for charity list view
    def test_unapproved_member_not_in_context(self):
        response = self.client.get(reverse('all_charities'))
        self.assertEqual(response.status_code, 200)
        test_user_2 = CustomUser.objects.get(username='test_user_2')
        self.assertFalse(test_user_2 in response.context['users'])

    # Test that the staff member does not appear in 'users' for charity list view
    def test_staff_member_not_in_context(self):
        response = self.client.get(reverse('all_charities'))
        self.assertEqual(response.status_code, 200)
        staff_member = CustomUser.objects.get(username='staff_member')
        self.assertFalse(staff_member in response.context['users'])

    def test_approved_member_charity_name_appears_in_content(self):
        response = self.client.get(reverse('all_charities'))
        self.assertEqual(response.status_code, 200)
        test_user_1 = CustomUser.objects.get(username='test_user_1')
        charity_name = test_user_1.charity_name
        self.assertTrue(charity_name in str(response.content))

    def test_approved_member_charity_bio_appears_in_content(self):
        response = self.client.get(reverse('all_charities'))
        self.assertEqual(response.status_code, 200)
        test_user_1 = CustomUser.objects.get(username='test_user_1')
        charity_bio = test_user_1.charity_bio
        self.assertTrue(charity_bio in str(response.content))

    # Pagination - test 'users' = '<Page 1 of 1>'
    def test_users_is_Page_1_of_1(self):
        response = self.client.get(reverse('all_charities'))
        self.assertTrue(str(response.context['users']) == '<Page 1 of 1>')
   
    # Test 'all_charities/?=page1' works for paginated charity_list view
    def test_page_1_status_code_is_200(self):
        response = self.client.get('/all_charities/?page=1')
        self.assertTrue(response.status_code == 200)





