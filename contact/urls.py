from django.urls import path

from .views import Contact
from . import views
app_name='contact'

urlpatterns = [

    path('', views.Contact,name='contact_data'),
]