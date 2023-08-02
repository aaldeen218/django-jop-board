from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.job_list,name='a'),
    path('<int:id>', views.job_detail),
]
