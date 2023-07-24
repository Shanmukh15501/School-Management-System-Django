
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import urlparse
from django.conf import settings
from django.contrib import messages
from CustomUser.models import Users
from SchoolManagement.forms import UserAuthenticationForm
from django.contrib.auth.decorators import login_required


from SchoolManagement.forms import UserRegistrationForm
from Common.Authentication import *
from django.contrib import auth
from django.contrib.auth import authenticate, login,logout




# @login_required
def my_view(request):
    if request.user.is_authenticated:
        # User is authenticated, you can access the user object
        user = request.user
        return HttpResponse(f"Hello, {user.email}!")
    else:
        print("else")
        user = request.user
        print("user",user)
        # User is anonymous
        return HttpResponse(f"Hello, {user}!")
    
    


def about(request):
 
    return render(request, 'about.html')



def contact(request):
 
    return render(request, 'contact.html')



def loginView(request):
    form = UserAuthenticationForm()
    if request.user.is_authenticated:
        pass
    if request.method == 'POST':


        

        form = UserAuthenticationForm(request.POST)
        email = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=email, password=password)
        login(request, user)
      

        if user:
            has_permission = user.has_perm('admin.view_logentry')
            context = {
                'email': email,
            'has_permission': has_permission,
            }
            
            request.session['email'] =  user.email
            request.session['role'] =  user.role
            

            return render(request, 'welcome.html', {'context': context})
        else:
            return render(request, 'login.html', {'form': form})

    elif request.method == 'GET':
         if 'email' in request.session:
             print(request.user)
             print(request.GET.get("user"))
             return render(request, 'welcome.html')
         else:
            return render(request, 'login.html', {'form': form})

    else:
        return render(request, 'login.html', {'form': form})

        

def Register(request):

    if request.method == 'POST': #if the form has been submitted
        form = UserRegistrationForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
 




def logout_view(request):
    print(request.session)
    logout(request)
    request.session.clear()
    return HttpResponseRedirect('/')





def selfuserdetails(request):
    print("REQUEST MODULE",request.session)
    return HttpResponseRedirect('/')



@login_required
def chatPage(request, *args, **kwargs):
    print("request.user",request.user)
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    return render(request, "chat.html", context)