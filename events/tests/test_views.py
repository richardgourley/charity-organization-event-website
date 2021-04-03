from django.test import TestCase
from datetime import datetime
from django.utils import timezone
from .models import Event
from accounts.models import CustomUser

class EventViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create CustomUser
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

        # Get test_user_1 - APPROVED USER
        test_user_1 = CustomUser.objects.get(username="test_user_1")
        # Get test_user_2 - UNAPPROVED USER
        test_user_2 = CustomUser.objects.get(username="test_user_2")

        # Create 3 Events
        Event.objects.create(
                user=test_user_1,
                event_name='Approved event',
                event_description='A lovely event.',
                event_date=timezone.now() + datetime.timedelta(days=10),
                event_url='http://www.testevent.com/approved_event',
                approved=True,
                image='image1.jpg',
                slug='88_test_charity_approved_event',
            )

        Event.objects.create(
                user=test_user_1,
                event_name='Unapproved event',
                event_description='Another lovely event.',
                event_date=timezone.now() + datetime.timedelta(days=10),
                event_url='http://www.testevent.com/unapproved_event',
                approved=False,
                image='image2.jpg',
                slug='88_test_charity_unapproved_event',
            )

        Event.objects.create(
                user=test_user_1,
                event_name='Date in the past event',
                event_description='An event with a date in the past.',
                event_date=timezone.now() - datetime.timedelta(weeks=6),
                event_url='http://www.testevent.com/date_in_the_past_event',
                approved=True,
                image='image3.jpg',
                slug='75_test_charity_date_in_the_past_event',
            )

        # Event somehow approved BUT created by unapproved user
        Event.objects.create(
                user=test_user_2,
                event_name="Unapproved user event",
                event_description="An event by unapproved user.",
                event_date=timezone.now() + datetime.timedelta(days=10),
                event_url='http://www.testevent.com/unapproved_user_event',
                approved=True,
                image='image4.jpg',
                slug='unapproved_user_event',
            )

    '''
    EVENT LIST VIEW TESTS
    '''
    def test_event_list_status_code_200(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)