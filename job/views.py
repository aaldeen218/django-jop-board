from django.shortcuts import render
from .models import  Job

# Create your views here.

def job_list(request):
    x={ 'all_job':Job.objects.all()}
    return render(request,'jobs.html',x)


def job_detail(request,id):
    x={ 'job':Job.objects.get(id=id)}
    return render(request,'job-details.html',x)
