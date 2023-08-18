from django.urls import path
from . import views


app_name='tests'

urlpatterns=[

    #path('test/',Test_class.as_view(),name='add_t'),
   # path('show_test/',Test_show_class.as_view(),name='show_t'),
     path('test/', views.test_show,name='name_test'),
     path('sub_test/<int:id>', views.subTest_a,name='name_subtest'),
    #path('s_test',SubTest_class.as_view(),name='add_sub'),
    #path('show_test/<int:x>',SubTest_class.as_view(),name='show_sub'),
]


