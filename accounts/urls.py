from django.urls import path
from django.contrib.auth import views as auth_views
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/',register, name='register'),
    path('token/', token_send, name='token'),
    path('verify/<uid>/<token>/', verify, name='verify'),
    path('password_change/', password_change, name='password_change'),
    path('login/', login_request, name='login'),
    path("logout", logout_request, name= "logout"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('forget_pwd/password_reset/',password_reset_request, name="password_reset"),
    path('forget_pwd/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='forget_pwd/password_reset_done.html'), name='password_reset_done'),
    path('forget_pwd/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="forget_pwd/password_reset_confirm.html"), name='password_reset_confirm'),
    path('forget_pwd/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='forget_pwd/password_reset_complete.html'), name='password_reset_complete'),
]
