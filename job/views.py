from django.shortcuts import render
from .models import  Job
from django.core.paginator import Paginator
from .form import ApplyForm

# Create your views here.

def job_list(request):
    job_list=Job.objects.all()  
    paginator=Paginator(job_list,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    

    context={ 'all_job':page_obj}
    return render(request,'jobs.html',context)

class Meta:
   ordering = ['-id']


def job_detail(request,id):
    job_id=Job.objects.get(id=id)
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_id
            myform.save()
    else:
        form=ApplyForm()
    x={ 'job':job_id,'form':form}
    return render(request,'job-details.html',x)

class Meta:
   ordering = ['id']
