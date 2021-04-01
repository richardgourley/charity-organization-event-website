from django.test import TestCase
from datetime import datetime
from django.utils import timezone
from .models import Event
from accounts.models import CustomUser

class EventModelTests(TestCase):
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

        # Get test_user_1
        test_user_1 = CustomUser.objects.get(username="test_user_1")

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

    def test_custom_user(self):
        custom_user_1 = CustomUser.objects.get(id=1)
        self.assertEqual(custom_user_1.username, "test_user_1")
        self.assertEqual(custom_user_1.charity_country.name, 'Australia')

    def test_event_user_username(self):
        event = Event.objects.get(event_name="Approved event")
        user = event.user
        self.assertEqual(user.username, 'test_user_1')

    def test_event_name_verbose_name(self):
        event = Event.objects.get(event_name="Approved event")
        field_label = event._meta.get_field('event_name').verbose_name
        self.assertEqual(field_label, 'event name')

    def test_event_name_max_length(self):
        event = Event.objects.get(event_name="Approved event")
        max_length = event._meta.get_field('event_name').max_length
        self.assertEqual(max_length, 255)

    def test_event_description_verbose_name(self):
        event = Event.objects.get(event_name="Approved event")
        field_label = event._meta.get_field('event_description').verbose_name
        self.assertEqual(field_label, 'event description')

    def test_event_date_verbose_name(self):
        event = Event.objects.get(event_name="Approved event")
        field_label = event._meta.get_field('event_date').verbose_name
        self.assertEqual(field_label, 'event date')

    def test_event_url_verbose_name(self):
        event = Event.objects.get(event_name="Approved event")
        field_label = event._meta.get_field('event_url').verbose_name
        self.assertEqual(field_label, 'event url')

    def test_event_url_help_text(self):
        event = Event.objects.get(event_name='Approved event')
        help_text = event._meta.get_field('event_url').help_text
        self.assertEqual(help_text, 'Enter a url users can visit to learn more.')

    def test_event_image_verbose_name(self):
        event = Event.objects.get(event_name="Approved event")
        field_label = event._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_event_image_uploads_to(self):
        event = Event.objects.get(event_name="Approved event")
        upload_to = event._meta.get_field('image').upload_to
        self.assertEqual(upload_to, 'events')

    def test_event_image_null_is_true(self):
        event = Event.objects.get(event_name="Approved event")
        null = event._meta.get_field('image').null
        self.assertEqual(null, True)

    def test_event_slug_null_is_false(self):
        event = Event.objects.get(event_name="Approved event")
        null = event._meta.get_field('slug').null
        self.assertEqual(null, False)

    def test_event_slug_unique_is_true(self):
        event = Event.objects.get(event_name="Approved event")
        unique = event._meta.get_field('slug').unique
        self.assertEqual(unique, True)

    def test_event_approved_field_default_is_false(self):
        event = Event.objects.get(event_name="Approved event")
        default = event._meta.get_field('approved').default
        self.assertEqual(default, False)

    def test_event_str(self):
        event = Event.objects.get(event_name="Approved event")
        event_str = event.__str__()
        self.assertEqual(event_str, 'Approved event')

    def test_event_str_equal_to_event_name(self):
        event = Event.objects.get(event_name="Approved event")
        self.assertTrue(event.__str__() == event.event_name)

    def test_event_get_absolute_url(self):
        event = Event.objects.get(event_name="Approved event")
        absolute_url = event.get_absolute_url()
        self.assertEqual(absolute_url, '/events/detail/88_test_charity_approved_event')





