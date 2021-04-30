# Charity Organization Sass

A SASS for charities written in Django and Wagtail.  
A charitable organization can create an account, add information about their charity and create charity events. 
The user can learn about charities and browse events based on the type of charity or can view charity events being held by a specific organization.

MODELS
There are 2 models in this app:
- Accounts - custom users created from the AbstractUser class
- Events

SKILLS COVERED
As well as typical Django models, templates and views, the app focusses heavily on using the AbstractUser class to extend the standard user model.

Hopefully this gives a good example to a new Django developer of the power of extending the base user class for many different types of user engagement apps.

The app also makes use of Django's excellent built-in password reset system if a user forgets a password - (see templates/registration)



