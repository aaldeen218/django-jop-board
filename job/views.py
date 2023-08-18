from django.shortcuts import redirect, render
from .models import  Job
from django.core.paginator import Paginator
from .form import ApplyForm,Job_add_form
from .filters import JobFilter
# Create your views here.

def job_list(request):
    job_list=Job.objects.all()  

    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs



    paginator=Paginator(job_list,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    

    context={ 'all_job':page_obj,'myfilter':myfilter}
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



def add_job(request):
    #job_id=Job.objects.get(id=id)
    if request.method=='POST':
        form=Job_add_form(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
        
        return redirect('jobs:add_job')
    else:
        form=Job_add_form()
        j=Job.objects.all()
    x={ 'form':form, 'j':j}
    return render(request,'job-add.html',x)




   
