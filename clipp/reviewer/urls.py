from django.contrib import admin
from django.urls import path, include
from reviewer import views

# app_name = 'reviewer'

urlpatterns = [
    path('', views.course, name="home"),
    path('create/', views.oldForm),
    path('list/<str:guid>/', views.dynamic_view, name="course-detail"),
    path('delete/<str:guid>/', views.delete),
    path('class/', views.CourseView.as_view())
   
]

