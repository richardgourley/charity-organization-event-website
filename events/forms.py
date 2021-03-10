from django import forms
from django.forms import ModelForm

from .models import Event

class EventForm(ModelForm):
	class Meta:
		model = Event
		exclude = ["user", "slug", "approved"]

		widgets = {
			'event_name':forms.TextInput(attrs={'class':'form-control mb-4 border'}),
			'event_description':forms.Textarea(attrs={'class':'form-control mb-4 border'}),
		}