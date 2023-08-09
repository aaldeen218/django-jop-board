from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SingupForm,UserForm,ProfileForm
from django.contrib.auth import authenticate,login
from .models import Profile

# Create your views here.
 
def Singup(request):
    if request.method=='POST':
        form=SingupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')

        
    else:
        form=SingupForm()
    return(render(request,'registration/singup.html',{'form':form}))




def profile(request):
    profile=Profile.objects.get(user=request.user)
    return(render(request,'registration/profile.html',{'profile':profile}))
   




def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform=UserForm(request.POST,instance=request.user)
        profile=ProfileForm(request.POST,request.FILES,instance=profile)    
        if userform.is_valid() and profile.is_valid():
            userform.save()
            myprofile=profile.save(commit=False)
            myprofile.user=request.user
            myprofile.save() 
            redirect(reverse("accounts_p:profile"))
         


    else:
        userform=UserForm(instance=request.user)
        profile=ProfileForm(instance=profile)

    return(render(request,'registration/profile_edit.html',{'userform':userform,'profile':profile,}))    