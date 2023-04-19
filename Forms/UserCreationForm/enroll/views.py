from django.shortcuts import render, HttpResponseRedirect
from .forms import Register, EditProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# User SignUp Function View
def register(request):
    if request.method == 'POST':
        obj = Register(request.POST)
        if obj.is_valid():
            obj.save()
        else:
            messages.error(
                request,
                'Plesase Enter Valid Credentials'
            )
    else:
        obj = Register()
    
    context = {
        'form': obj
    }
    return render(request, 'index.html', context=context)


# User Login Function View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            obj = AuthenticationForm(request=request, data=request.POST)
            if obj.is_valid():
                username = obj.cleaned_data['username']
                password = obj.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully!!!!!')
                    return HttpResponseRedirect('/profile/')
        else:
            obj = AuthenticationForm()
        context = {
            'form':obj,
        }
        return render(request, 'login.html', context=context)
    else:
        return HttpResponseRedirect('/profile/')

# User Profile View
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = EditProfileForm(request.POST, instance=request.user)
            if obj.is_valid():
                obj.save()
                messages.success(request, 'Profile Updated Successfully!!!!!')
        else:
            obj = EditProfileForm(instance=request.user)
        context = {
            'form': obj,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name

        }
        return render(request, 'profile.html', context=context)
    else:
        return HttpResponseRedirect('/login/')

# User LogOut View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Password change with old password view
"""
NOTE:
    - PasswordChangeForm is used to change password with old password =>(example below)
    - SetPasswordForm is used to change password without old password =>(not use yet)
"""
def change_password(request):
    if request.method == 'POST':
        obj = PasswordChangeForm(user=request.user, data=request.POST)
        if obj.is_valid():
            obj.save()
            #NOTE: update session auth hash is used because when we change password, the session is interupted and redirect to login page but we need to redirect it to profile page
            update_session_auth_hash(request, request.user) 
            return HttpResponseRedirect('/profile/')
    else:
        obj = PasswordChangeForm(user=request.user)
    context = {
        'form': obj
    }
    return render(request, 'password.html', context=context)