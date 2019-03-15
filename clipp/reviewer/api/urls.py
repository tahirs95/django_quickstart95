from django.contrib import admin
from django.urls import path
from reviewer.api.views import (
    CourseListAPIView,
    CourseRetrieveAPIView,
    CourseDeleteAPIView,
    CourseUpdateAPIView,
    CourseCreateAPIView,
) 

urlpatterns = [
    path('course/', CourseListAPIView.as_view()),
     path('course/create/', CourseCreateAPIView.as_view()),
    path('course/<pk>/', CourseRetrieveAPIView.as_view()),
    path('course/<pk>/edit/', CourseUpdateAPIView.as_view()),
    path('course/<pk>/delete/', CourseDeleteAPIView.as_view()),

]