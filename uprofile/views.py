from django.shortcuts import render, redirect, get_object_or_404
from . models import Profile
from. models import Account
from . forms import ProfileForm
from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_http_method
from django.views.decorators.http import require_http_methods
# from django.contrib.auth.decorators import login_required


def profile(request):
    profile = request.user.profile
    # user = Profile.objects.filter(request.user.id).values(id)
    users = Profile.objects.get(username=request.user)
    print(users)
    print(users.phone)
    return render(request, 'profile.html', {'profile':profile, 'users':users})


def profile_edit(request):
    user = request.user.profile
    form = ProfileForm(request.POST or None,instance=user)
    if request.method=='POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=request.user
            profile.save()
            print("Profile is here.")
            print(profile.first_name)
            print(profile.profile_image)
            return redirect('profile')
    return render(request, 'profile_edit.html', {'form':form, 'user':user})

from django.contrib.auth import logout as auth_logout, get_user_model

@login_required
@require_http_methods(['POST'])
def delete_user_profile(request):
    pk = request.user.pk
    # auth_logout(request)
    account = get_user_model()
    Account.objects.filter(pk=account.pk).delete()
