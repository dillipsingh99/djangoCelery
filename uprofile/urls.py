from django.urls import path
from . views import *

urlpatterns = [
    path('', profile, name='profile'),
    path('edit/', profile_edit, name="profile_edit"),
    path('delete/', delete_user_profile, name='delete_user_profile'),
]
