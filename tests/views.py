from audioop import reverse
from typing import Any, Dict
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import SubTest,Test
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
    print(j)
    if request.method=='POST':
        form=Form_SubTest(request.POST,request.FILES)
        if form.is_valid():
            #myform=form.save()
           # myform.owner=request.user
           form.save()
        
        return redirect('test_:name_subtest',id)
    else:
        form=Form_SubTest()
        
        x={ 'form':form, 'y':j}
    return render(request,'show_subTest.html',x)


























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


