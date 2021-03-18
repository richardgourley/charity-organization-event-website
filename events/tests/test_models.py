from django.test import TestCase
from datetime import datetime
from .models import Event
from accounts.models import CustomUser

class EventModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create CustomUser
        CustomUser.objects.create(
                username="test_user_1",
                email="email@testcharity.com",
                password='test_user_2',
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
                approved=False,
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

    def test_custom_user(self):
        custom_user_1 = CustomUser.objects.get(id=1)
        self.assertEqual(custom_user_1.username, "test_user_1")
        self.assertEqual(custom_user_1.charity_country.name, 'Australia')

    def test_event_name_verbose_name(self):
        event = Event.objects.get(event_name="Approved event")
        field_label = event._meta.get_field('event_name').verbose_name
        self.assertEqual(field_label, 'event name')
