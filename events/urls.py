from django.urls import path
from .views import EventListView, EventDetailView, update_event_view, create_event_view

app_name = 'events'
urlpatterns = [
    path('', EventListView.as_view(), name='all_events'),
    path('update/<slug:slug>', update_event_view, name='update_event'),
    path('detail/<slug:slug>', EventDetailView.as_view(), name='event_detail'),
    path('create/', create_event_view, name='create_event'),
]