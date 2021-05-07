# Charity Organization Event Website

A login event management system for charities written in Django and Wagtail with full Django login, signup and password reset functionality.

A charitable organization can create an account, add information about their charity and create charity events. 

The user can learn about charities and browse events based on the type of charity or can view charity events being held by a specific organization.

Charities and events are subject to approval before appearing on the website.

MODELS
There are 2 models in this app:
- Accounts 
    - CustomUser can add charity information to their account.
    - CustomUser inherits from AbstractUser.
- Events

# SKILLS COVERED
As well as standard Django models, views and templates I've listed all tools and modules used within the application to help Django students see if this repo has some modules they would like to learn more about:

## GENERAL
python-decouple and a '.env' file - 
  - used to avoid displaying database and secret key information if deploying to Github
AUTH_USER_MODEL = 'accounts.CustomUser' - setting up an AUTH_USER_MODEL

## ACCOUNTS
- Custom User class inheriting the built in 'AbstractUser' class
  - Extending the standard Django users is key to this application.  It allows the
    developer to create any type of user application by adding fields to the existing Django
    user fields.
- django_countries - adding a select field of all countries to a form
- choices within a charfield
- ImageField

- django auth forms - UserCreationForm, UserChangeForm
- widgets - attrs - allows CSS styling of forms
- ModelForm

- SimpleUploadedFile from django.core.files.uploadedfile
- reverse
- reverse_lazy
- generic views
- HttpResponseRedirect
- Paginator, EmptyPage, PageNotAnInteger
- Pagination for function based views

- auth.decorators - login_required

- pagination in templates - obj.has_previous and obj.has_next used in charity list template

## EVENTS
SlugField
reverse 
ForeignKey - including settings.AUTH_USER_MODEL to assign CustomUser to an Event object.
timezone  - used in bespoke model method - 'date_in_future'

ModelForm
widgets - attrs - add css styling to a form
slug - used as part of a URL
generic - ListView, DetailView
Paginator - generic class based views

## HOME
template tags - adding Python to a part of a web page, in this case footer
register = template.Library()
@register.inclusion_tag("tags/footer.html")

## REGISTRATION
Using Django's built in registration templates:
- login.html
- password_reset_completed.html
- password_reset_confirm.html
- password_reset_done.html
- password_reset_form.html

## TESTING
- TestCase
- 200 and 302 status code testing
- login - testing logged in users actions
- Model and View Testing
- Timezone and datetime.timedelta() - used to create dates in the future and the past for testing model instances
- self.client - used to retrieve the html content and context variables to test site pages
- meta - used to test individual model fields
- assertion methods - asserTrue, assertFalse, assertEqual, assertTemplateUsed
- response.content() and response.context()


