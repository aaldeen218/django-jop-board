from django.shortcuts import render
from .forms import PatientForm

# Create your views here.
def addNewPatient(request):
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()        
    else:
        form=PatientForm()
    return(render(request,'add_patient.html',{'form':form}))