from django.urls import include, path
from .forms import SingupForm
from . import views

app_name="account"
urlpatterns=[

   path('singup',views.Singup,name='singup' ),
   path('profile/',views.profile,name='profile' ),
   path('profile/profile_edit/',views.profile_edit,name='profile_edit' ),

]