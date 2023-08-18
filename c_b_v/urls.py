from django.urls import path
from .views import *
app_name='c_b_v'
urlpatterns = [
    path("show/", show.as_view(),name='show'),
    path("add_data/", add_data.as_view(),name='add_data'),
]