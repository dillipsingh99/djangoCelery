from django.shortcuts import render, redirect
from . models import Account
from . forms import RegistrationForm
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import messages
from . forms import SetPasswordForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.core.mail import BadHeaderError


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = user.email
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            send_mail_after_registration(email, uid, token)
        return redirect('token')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html', {'form':form})

def send_mail_after_registration(email, uidb64, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{uidb64}/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail(subject, message , email_from ,recipient_list )


def token_send(request):
    return render(request, 'accounts/token.html')


def verify(request, uid, token):
    uidb64 = uid
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = Account.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for email verification.')
        return redirect('password_reset_confirm', uidb64, token)
    else:
        messages.error(request, 'Activation link is invalid!')
    messages.success(request, 'Your account is verified. Now you can log into your Account.')
    return redirect('login')


@login_required
def password_change(request):
    user = request.user
    if request.method=="POST":
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your password has been created.')
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = SetPasswordForm(user)
    return render(request, 'accounts/change_password.html', {'form':form})

def login_request(request):
    logout(request)
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Successfully logged into your accounts.')
                return redirect('index')
    messages.success(request, 'Log into your accounts.')
    return render(request, 'accounts/login.html')


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = Account.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "forget_pwd/password_reset_email.txt"
                    c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name':'Website',
                        "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'hitlerdeepak1995@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/forget_pwd/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="forget_pwd/password_reset.html", context={"password_reset_form":password_reset_form})