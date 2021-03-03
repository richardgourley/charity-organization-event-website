from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic

from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm, CustomUserChangeForm, EditCustomUserProfileForm
from .models import CustomUser
from events.models import Event

from django.http import HttpResponseRedirect
from django.urls import reverse

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

# Custom user can update information about their charity (but not their username and password)
@login_required
def edit_custom_user_profile(request):
    current_user = CustomUser.objects.get(id=request.user.id)
    
    if request.method == "POST":
        form = EditCustomUserProfileForm(request.POST)
        if form.is_valid():
            current_user.charity_name = form.cleaned_data['charity_name']
            current_user.charity_address_line_1 = form.cleaned_data['charity_address_line_1']
            current_user.charity_address_line_2 = form.cleaned_data['charity_address_line_2']
            current_user.charity_postcode = form.cleaned_data['charity_postcode']
            current_user.charity_website_url = form.cleaned_data['charity_website_url']
            current_user.charity_bio = form.cleaned_data['charity_bio']
            current_user.charity_country = form.cleaned_data['charity_country']
            current_user.charity_operating_continent = form.cleaned_data['charity_operating_continent']
            current_user.save()
            return HttpResponseRedirect(reverse('accounts:profile'))
        else:
            context = {
                'form':form
            }
    else:
        data = {
            'charity_name':current_user.charity_name,
            'charity_address_line_1':current_user.charity_address_line_1,
            'charity_address_line_2':current_user.charity_address_line_2,
            'charity_postcode':current_user.charity_postcode,
            'charity_website_url':current_user.charity_website_url,
            'charity_bio':current_user.charity_bio,
            'charity_country':current_user.charity_country,
            'charity_operating_continent':current_user.charity_operating_continent,
        }
        form = EditCustomUserProfileForm(initial=data)
        
        context = {
            'form':form
        }

    return render(request, 'registration/edit_custom_user_profile.html', context=context)

@login_required
def account_profile_page(request):
    current_user = CustomUser.objects.get(id=request.user.id)

    events = Event.objects.all().filter(user=current_user)
    num_events = str(len(events))

    context = {
        'current_user':current_user,
        'events':events,
        'num_events':num_events
    }
    return render(request, 'accounts/profile.html', context=context)


