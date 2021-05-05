from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.contrib.auth.decorators import login_required

from .models import Event
from .forms import EventForm
from accounts.models import CustomUser

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.utils import timezone

import random

# Event list view
class EventListView(generic.ListView):
    model = Event
    template_name = 'events/all_events.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.all().filter(approved=True).filter(event_date__gte=timezone.now()).order_by('event_date')

# Event Detail View
class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'events/event_detail.html'

    def get_queryset(self):
        return Event.objects.all().filter(approved=True).filter(event_date__gte=timezone.now())

# Create an event view
@login_required
def create_event_view(request):
    current_user = CustomUser.objects.get(id=request.user.id)

    if current_user.is_staff == True:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            charity_name = current_user.charity_name
            event_name = form.cleaned_data['event_name']
            event = Event.objects.create(
                user = current_user,
                event_name = event_name,
                event_description = form.cleaned_data['event_description'],
                event_date = form.cleaned_data['event_date'],
                event_url = form.cleaned_data['event_url'],
                image = form.cleaned_data['image'],
                slug = slugify_event_name(charity_name, event_name)
            )
            event.save()
            return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        initial_form_data = {'event_date':'MM/DD/YYYY', 'event_url':'http://'}
        form = EventForm(initial=initial_form_data)

    return render(request, 'events/create_event.html', context={'user':current_user, 'form':form})

# Edit an event view
@login_required
def update_event_view(request, slug):
    obj = get_object_or_404(Event, slug=slug)
    current_user = CustomUser.objects.get(id=request.user.id)

    if current_user.is_staff == True:
        return HttpResponseRedirect('/')

    # Check logged in user is 'user' of this event
    if obj.user != current_user:
        return HttpResponseRedirect(reverse('accounts:profile'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj.event_name = form.cleaned_data['event_name']
            obj.event_description = form.cleaned_data['event_description']
            obj.event_date = form.cleaned_data['event_date']
            obj.event_url = form.cleaned_data['event_url']
            obj.image = form.cleaned_data['image']
            obj.save()
            return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        form = EventForm(request.POST or None, request.FILES or None, instance=obj)

    return render(request, 'events/update_event.html', context={'form':form})

'''
@ returns - string
Combines Random number + charity name + event name joined with '_' for uniqueness
'''
def slugify_event_name(charity_name, event_name):
    random_num = random.randint(10,99)
    split_names = (charity_name.lower()).split(' ') + (event_name.lower()).split(' ')
    slug = str(random_num) + ('_') + ('_').join(split_names)
    return str(slug)


