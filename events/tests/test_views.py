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

    def test_event_list_reverse_url_status_code_200(self):
        response = self.client.get(reverse('events:all_events'))
        self.assertEqual(response.status_code, 200)

    def test_event_list_correct_template_used(self):
        response = self.client.get(reverse('events:all_events'))
        self.assertTemplateUsed(response, 'events/all_events.html')

    def test_event_list_approved_event_appears_in_content(self):
        response = self.client.get(reverse('events:all_events'))
        self.assertTrue('Approved event' in str(response.content))
        self.assertTrue('88_test_charity_approved_event' in str(respone.content))

    def test_event_list_unapproved_event_doesnt_appear_in_content(self):
        response = self.client.get(reverse('events:all_events'))
        self.assertFalse('Unapproved event' in str(response.content))
        self.assertFalse('88_test_charity_unapproved_event' in str(response.content))

    def test_event_list_date_in_the_past_event_doesnt_appear_in_content(self):
        response = self.client.get(reverse('events:all_events'))
        self.assertFalse('Date in the past event' in str(response.content))
        self.assertFalse('75_test_charity_date_in_the_past_event' in str(response.content))

    def test_event_list_approved_event_appears_in_context(self):
        event = Event.objects.get(event_name="Approved event")
        self.assertTrue(event in response.context['object_list'])

    def test_event_list_unapproved_event_doesnt_appear_in_context(self):
        event = Event.objects.get(event_name="Unapproved event")
        self.assertFalse(event in response.context['object_list'])

    def test_event_list_date_in_the_past_event_doesnt_appear_in_context(self):
        event = Event.objects.get(event_name="Date in the past event")
        self.assertFalse(event in response.context['object_list'])

    '''
    EVENT DETAIL VIEW TESTS
    '''

    def test_detail_view_status_code_200_approved_event(self):
        response = self.client.get('/events/detail/88_test_charity_approved_event')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_status_code_200_approved_event_reverse_url(self):
        event = Event.objects.get(event_name='Approved event')
        response = client.get(reverse('events:event_detail', args=(event.slug,)))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_correct_template_used(self):
        response = self.client.get('/events/detail/88_test_charity_approved_event')
        self.assertTemplateUsed(response, 'events/event_detail.html')

    def test_detail_view_unapproved_event_detail_view_returns_404(self):
        response = self.client.get('/events/detail/88_test_charity_unapproved_event')
        self.assertEqual(response.status_code, 404)

    def test_detail_view_unapproved_user_event_detail_view_returns_404(self):
        response = self.client.get('/events/detail/97_unapproved_user_event')
        self.assertEqual(response.status_code, 404)

    def test_detail_view_date_in_past_event_detail_view_returns_404(self):
        response = self.client.get('/events/detail/75_test_charity_date_in_the_past_event')
        self.assertEqual(response.status_code, 404)

    def test_detail_view_approved_event_content_charity_name_appears(self):
        response = self.client.get('/events/detail/88_test_charity_approved_event')
        self.assertTrue('Test Charity' in str(response.content))

    def test_detail_view_approved_event_content_event_description_appears(self):
        response = self.client.get('/events/detail/88_test_charity_approved_event')
        self.assertTrue('A lovely event.' in str(response.content))

    def test_detail_view_approved_event_content_event_url_appears(self):
        response = self.client.get('/events/detail/88_test_charity_approved_event')
        self.assertTrue('http://www.testevent.com/approved_event' in str(response.content))

        # Check that the date appearing on the page is in expected format
    def test_detail_view_approved_event_date_appears_correct_format(self):
        # Expecting this format: Oct. 8, 2020
        event = Event.objects.get(event_name='Approved event')
        response = self.client.get('/events/detail/88_test_charity_approved_event/')
        event_date = event.event_date
        formatted_date = event_date.strftime("%b") + ". " + event_date.strftime("%d") + ", " + event_date.strftime("%Y") 
        self.assertTrue(formatted_date in str(response.content))

    '''
    CREATE EVENT VIEW TESTS
    '''
    def test_create_event_view_not_logged_in_redirects(self):
        response = self.client.get('/events/create/')
        self.assertTrue(response.status_code, 302)

    def test_create_event_view_logged_in_status_code_200(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get('/events/create/')
        self.assertTrue(response.status_code, 302)

    def test_create_event_view_logged_in_reverse_url_status_code_200(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('events:create_event'))
        self.assertTrue(response.status_code, 302)

    def test_create_event_view_logged_in_correct_template_used(self):
        login = self.client.login(username='test_user_1', password='test_user_1')
        response = self.client.get(reverse('events:create_event'))
        self.assertTemplateUsed(response, 'events/create_event.html')

    def test_create_event_view_staff_member_logged_in_redirects(self):
        login = self.client.login(username='staff_member', password='staff_member')
        response = self.client.get(reverse('events:create_event'))
        self.assertEqual(response.status_code, 302)

    def test_create_event_view_unapproved_user_logged_in_redirects(self):
        login = self.client.login(username='test_user_2', password='test_user_2')
        response = self.client.get(reverse('events:create_event'))
        self.assertEqual(response.status_code, 302)
