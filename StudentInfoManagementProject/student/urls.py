# map view to url

from django.urls import path
from . import views

#url configuration
urlpatterns = [
    path('info/', views.studentInfo),
    path('info/add', views.studentInfoAdd),
    path('info/delete/', views.studentInfoDel),
]