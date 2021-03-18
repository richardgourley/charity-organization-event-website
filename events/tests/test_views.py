from django.test import TestCase
from datetime import datetime
from .models import Event
from accounts.models import CustomUser

'''
VIEW TESTS
'''
class EventViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)