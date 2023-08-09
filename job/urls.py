from django.contrib import admin
from django.urls import include, path
from . import views
app_name='job'
urlpatterns = [

    path('', views.job_list,name='all_jobs'),
    path('add/', views.add_job,name='add_job'),
    
    path('<int:id>', views.job_detail,name='job_detail'),
]
