from django.urls import path
from . import views
urlpatterns =[

    #----- Ckeditor ----- 
    path ('',views.insertPost ,name='insertUrl'),
    path('post/<str:pk>/', views.post, name="post"),
    path ('edit/<str:pk>',views.editPost ,name='editUrl'),

]