
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse
from urllib.parse import urlparse
from django.conf import settings

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
 
    return render(request, 'login.html')


def Register(request):
 
    return render(request, 'register.html')
