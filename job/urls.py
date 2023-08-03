from django.contrib import admin
from django.urls import include, path
from . import views
app_name='job'
urlpatterns = [
    path('', views.job_list,name='a'),
    path('add', views.add_job,name='a'),
    
    path('<int:id>', views.job_detail,name='job_detail'),
]
