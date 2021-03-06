from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
	model = Event
	list_display = ['user', 'event_name', 'approved']
	fields = [
		'user',
		'event_name',
		'event_description',
		'event_date',
		'event_url',
		'approved',
		'image',
		'slug',
	]


admin.site.register(Event, EventAdmin)