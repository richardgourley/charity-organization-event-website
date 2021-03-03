from django.urls import path
from .views import SignUpView, edit_custom_user_profile, account_profile_page

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('editprofile/', edit_custom_user_profile, name='editprofile'),
    path('profile/', account_profile_page, name='profile'),
]