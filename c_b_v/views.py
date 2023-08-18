from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from .models import Student


# Create your views here.
class show(ListView):
    all_std=Student.objects.all()
    model=Student
    template_name = "student_list.html"
    #queryset =all_std.filter(name__exact='Alaa')
    ordering=['-create_at']


class add_data(CreateView):
    model=Student
    fields=['name','age'] 
    template_name= 'student_form.html'
    success_url=reverse_lazy('c_b_v:show')
    


    def get_form_kwargs(self):
        kwargs = {
        "initial": self.get_initial(),
        "prefix": self.get_prefix(),
      }
        if self.request.method in ("POST", "PUT"):
             kwargs.update(
            {

                "data": self.request.POST,
                "files": self.request.FILES,
            }
           
        )
        
             
        return kwargs
   
    