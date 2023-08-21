from audioop import reverse
from typing import Any, Dict
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import SubTest,Test,Check
from .form import *




#from django.views.generic import ListView,CreateView

def test_show(request):
    if request.method=='POST':
        form=Form_Test(request.POST,request.FILES)
        if form.is_valid():
            #myform=form.save()
           # myform.owner=request.user
           form.save()
        
        return redirect('test_:name_test')
    else:
        form=Form_Test()
        j=Test.objects.all()
        x={ 'form':form, 'y':j}
    return render(request,'show_test.html',x)




def subTest_a(request,id):
    j=SubTest.objects.filter(test_name=id)
    ee=Test.objects.get(pk=id)
    print(ee)
    if request.method=='POST':
        form=Form_SubTest(request.POST,request.FILES)
        if form.is_valid():
           myform=form.save(commit=False)
           myform.test_name=Test.objects.get(pk=id)
           
           myform.save()
        
        return redirect('test_:name_subtest',id)
    else:
        form=Form_SubTest()
        
        x={ 'form':form, 'y':j,'ee':ee}
    return render(request,'show_subTest.html',x)

def patient_add(request):
      if request.method=='POST':
        form=Form_Patient(request.POST)
        if form.is_valid():
            #myform=form.save()
           # myform.owner=request.user
           form.save()
        
        return redirect('test_:check_add')
      else:
        form=Form_Patient()
        j=Patient.objects.all()
        x={ 'form':form, 'y':j}
      return render(request,'patient_add.html',x)




def check_add(request):
    j=Check.objects.filter().order_by('-id')
    ee=j


    if request.method=='POST':
        form=Form_Check(request.POST)
        if form.is_valid():
           form.save()
        
        return redirect('test_:check_add')
    else:
        form=Form_Check()
        
        x={ 'form':form, 'y':j,'ee':ee}
    return render(request,'check_add.html',x)


def result_add(request,id):
    print(id)
    j=Check_items.objects.filter(check_id=id)
    f=j.first()
    print(f)
    
    ee=j
    #data=Form_Check(instance=f)
    # data = get_object_or_404(f)
    # Check_items.objects.all().update(check_result="8")
    print("Edit")

    
    # print(request)


    if request.method=='POST':
        table_data = request.POST.get('table_data')
        # print(table_data)

        part_one_str,part_tow_str=str(table_data).split('$$')
        part_one_str=part_one_str.replace("\"","")
        # print(part_tow_str)

        part_one_List=part_one_str.split(",")

        part_tow_str=part_tow_str.replace("\\n","")
        part_tow_str = ''.join(part_tow_str.split())
        part_tow_str=part_tow_str.replace("\"","")

        part_tow_List=part_tow_str.split(",")

        # print(part_tow_List)
       
        for j in range(0,len(part_one_List),1):
            # print((part_tow_List[j]))
            
            Check_items.objects.filter(id=int(part_one_List[j])).update(check_result=part_tow_List[j]) 
           
       




        
        form=Form_Check_items(request.POST,instance=f)
        if form.is_valid():
           #form.save()
        
         return redirect('test_:result_add')
    else:
        form=Form_Check_items(instance=f)
        
        x={ 'form':form, 'y':j,'f':f}
    return render(request,'result_add.html',x)


def result_list(request):
    j=Check.objects.filter().order_by("-id")
    
    x={'y':j}
    return render(request,'result_list.html',x)    


















# class Test_show_class(CreateView):
#     model=Test
#     template_name='show_test.html'
#     #context_object_name='y' 
#     context_object_name='form'    
#     fields=('__all__')  
#     y=Test.objects.all()
#     extra_context={'y':y}

#     success_url=reverse_lazy('name_test:show_t')
#         #return Test.objects.all(test_name=self.kwargs.get('q'))   

# class SubTest_class(CreateView):
#     xc=''
#     model=SubTest
#     template_name='show_subTest.html'
#     x=SubTest.objects.all()
#     y=x 
#     context_object_name='form'
#     extra_context={'x':x,'y':y}    
#     fields=('__all__')
    
#     success_url=reverse_lazy('name_test:show_sub',kwargs={'x':5})

#     def get_initial(self) -> Dict[str, Any]:
#         initial= super().get_initial()
#         initial['sub_name']="Enter SubTest Name"
#         return initial

#     def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
#         xc=kwargs['x']
#         return super().get(request, *args, **kwargs)

