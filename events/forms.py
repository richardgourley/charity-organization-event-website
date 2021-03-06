from django import forms
from django.forms import ModelForm

from .models import Event

class EventForm(ModelForm):
	class Meta:
		model = Event
		exclude = ["user", "slug"]