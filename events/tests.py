from django.test import TestCase
from datetime import datetime
from .models import Event
from accounts.models import CustomUser

class EventTests(TestCase):
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
                charity_website_url="testcharity.com",
                charity_bio="A test charity number 1",
                charity_country='AU',
                charity_operating_continent="oc",
            )

        # Get test_user_1
        test_user_1 = CustomUser.objects.get(username="test_user_1")

        # Create 3 Events
        Event.objects.create(
                user=test_user_1,
                event_name='Approved event',
                event_description='A lovely event.',
                event_date=datetime.strptime("8-10-2021", "%d-%m-%Y"),
                event_url='http://www.testevent.com/approved_event',
                approved=True,
                image='image1.jpg',
                slug='88_test_charity_approved_event',
            )

        Event.objects.create(
                user=test_user_1,
                event_name='Unapproved event',
                event_description='Another lovely event.',
                event_date=datetime.strptime("5-5-2021", "%d-%m-%Y"),
                event_url='http://www.testevent.com/unapproved_event',
                approved=True,
                image='image2.jpg',
                slug='88_test_charity_unapproved_event',
            )

        Event.objects.create(
                user=test_user_1,
                event_name='Date in the past event',
                event_description='An event with a date in the past.',
                event_date=datetime.strptime("8-10-2020", "%d-%m-%Y"),
                event_url='http://www.testevent.com/date_in_the_past_event',
                approved=True,
                image='image3.jpg',
                slug='75_test_charity_date_in_the_past_event',
            )


