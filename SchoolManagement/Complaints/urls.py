from django.urls import path
from .views import *

urlpatterns = [
    path('new' , newComplaint,name='newComplaint'),
    path('view' , viewComplaint,name='viewComplaint'),
    path('edit/<int:id>' , editComplaint,name='editComplaint'),
    path('delete/<int:id>' , deleteComplaint,name='deleteComplaint'),
]