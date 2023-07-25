from django.shortcuts import render, HttpResponseRedirect
from .models import ComplaintsData
from .forms import ComplaintForm
# Create your views here.

def newComplaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            complaintAgainst = form.cleaned_data['complaintAgainst']
            complaintDetails = form.cleaned_data['complaintDetails']
            obj = ComplaintsData(name=name, email=email, complaintAgainst=complaintAgainst, complaintDetails=complaintDetails)
            # to save formdata in DB
            obj.save()
            # to reset form
            form = ComplaintForm()
    else:
        form = ComplaintForm()
    return render(request, 'complaint.html', {'forms': form })

# Fuction to show complaints
def viewComplaint(request):
    complaints = ComplaintsData.objects.all()
    return render(request, 'viewComplaint.html', {'complaints': complaints})

# function to delete Complaint
def deleteComplaint(request, id):
    if request.method == 'POST':
        obj = ComplaintsData.objects.get(pk=id)
        obj.delete()
        complaints = ComplaintsData.objects.all()
        return HttpResponseRedirect('/complaint/view')
    
# function to edit/update Complaint
def editComplaint(request, id):
    if request.method == 'POST':
        obj = ComplaintsData.objects.get(pk=id)
        form = ComplaintForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            complaints = ComplaintsData.objects.all()
            return render(request, 'viewComplaint.html', {'complaints': complaints})
    elif request.method == 'GET':
        obj = ComplaintsData(name=request.get("name"))
        # obj = ComplaintsData.objects.get(pk=id)
        form = ComplaintForm(instance=obj)
    return render(request, 'editComplaint.html', {'forms':form})