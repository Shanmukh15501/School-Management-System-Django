
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import urlparse
from django.conf import settings
from django.contrib import messages
from CustomUser.models import Users
from SchoolManagement.forms import UserAuthenticationForm

from SchoolManagement.forms import UserRegistrationForm
from Common.Authentication import *
from django.contrib import auth
from django.contrib.auth import logout



# Create your views here.
def index_view(request):

    # full_path = request.get_full_path()
    # full_path = "" if full_path == "/" else full_path
    baseurl = "https://" if request.is_secure() else "http://"
    baseurl += request.get_host() # + full_path
    print("baseurl",baseurl)

    # iobaseurl = "wss://" if request.is_secure() else "ws://"
    # iobaseurl += urlparse(baseurl).hostname

    return render(request, "index.html", {'baseurl': baseurl})


def about(request):
 
    return render(request, 'about.html')



def contact(request):
 
    return render(request, 'contact.html')



def login(request):
    form = UserAuthenticationForm()
    if request.method == 'POST':

        form = UserAuthenticationForm(request.POST)
        email = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user:
            return render(request, 'welcome.html', {'email': email})
        else:
            return render(request, 'login.html', {'form': form})

    else:
        return render(request, 'login.html', {'form': form})

        

def Register(request):

    if request.method == 'POST': #if the form has been submitted
        form = UserRegistrationForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
 




def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


