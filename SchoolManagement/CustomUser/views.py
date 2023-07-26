
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import urlparse
from django.conf import settings
from django.contrib import messages
from CustomUser.models import Users
from CustomUser.serializers import UserCommonSerializer
from SchoolManagement.forms import UserAuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView







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
            # has_permission = user.has_perm('admin.view_logentry')
            context = {
                'email': email,
            }
            
            request.session['email'] =  user.email
            request.session['role'] =  user.role
            
            print("context",context)
            return render(request, 'welcome.html',context)
        else:
            return render(request, 'login.html', {'form': form})

    elif request.method == 'GET':
         print(" request.session",request.session)
         if 'email' in request.session:
             
             print(request.user)
             context = {
                'email': request.session['email'],
            }
             return render(request, 'welcome.html',context)
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


class IamUserDetails(generics.RetrieveAPIView):
    permission_classes =[permissions.AllowAny]
    serializer_class = UserCommonSerializer
    queryset = User.objects.all()

    def get_object(self):
        # Get the 'id' value from the URL parameters
        id_value = self.kwargs.get('id')

        # Use the 'id' value to retrieve the user object
        obj = User.objects.get(pk=id_value)
        self.check_object_permissions(self.request, obj)
        return obj



class UserActive_Inactive(APIView):

    permission_classes = [permissions.AllowAny]
    
    def post(self, request,*args, **kwargs):
        id = kwargs['id']
        try:
            user = User.objects.get(id=id)
            if user.is_active:
                user.is_active=False
                user.save()
                return Response({"user":' User Inactivated'}, status=status.HTTP_200_OK)
            else:
                 
                user.is_active=True
                user.save()
                return Response({"user":' User Activated'}, status=status.HTTP_200_OK)

         

        except User.DoesNotExist:
            return Response({"user":'user does not exists'}, status=status.HTTP_200_OK)