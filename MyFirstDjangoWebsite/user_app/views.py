from django.shortcuts import render
from user_app.forms import UserForm,UserProfileInfoForm


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def userindex(request):
    return render(request,"user_app/userindex.html")

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request,"user_app/register.html",{'user_form':user_form, 'profile_form':profile_form, 'registered':registered})




def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('user_app:userindex'))

            else:
                return HttpResponse("USER NOT ACITVE")

        else:
            print("SOME1 TRIED TO LOGIN BUT FAILED")
            return HttpResponse("INVALID LOGIN DETAILS")

    else:
        return render(request,"user_app/login.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_app:userindex'))

@login_required
def special(request):
    return HttpResponse("NICE YOU ARE LOGGED IN")
