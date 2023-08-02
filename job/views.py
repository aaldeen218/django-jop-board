from django.shortcuts import render
from .models import  Job

# Create your views here.

def job_list(request):
    x={ 'all_job':Job.objects.all()}
    return render(request,'job_list.html',x)


def job_detail(request):
    x=('all_job',Job.objects.all())
    return render(request,x)
