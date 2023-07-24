
from django.shortcuts import render

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
