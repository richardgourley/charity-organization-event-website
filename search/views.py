from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.core.models import Page
from wagtail.search.models import Query

from events.models import Event
from accounts.models import CustomUser

from django.utils import timezone


def search_events(request):
    search_query = request.GET.get('query', None)

    # Gets current paginated page
    page = request.GET.get('page', 1)

    if search_query:
        events = Event.objects.all().filter(approved=True).filter(event_date__gte=timezone.now()).filter(event_name__icontains=search_query)
    else:
        events = []

    paginator = Paginator(events, 1)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    display_pagination = False

    if events.paginator.num_pages > 1:
        display_pagination = True

    return TemplateResponse(request, 'search/search_events.html', {
        'search_query':search_query,
        'events':events,
        'display_pagination': display_pagination,
        'page':page
    })
