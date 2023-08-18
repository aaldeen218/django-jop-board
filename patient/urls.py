from django.urls import path
from . import views

app_name='patient'

urlpatterns=[

path('add_patient/',views.addNewPatient,name='add_patient'),

]