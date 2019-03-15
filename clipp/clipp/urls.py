"""clipp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reviewer import views

# app_name = 'reviewer'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include(('reviewer.urls', 'reviewer'), namespace='reviewer')),
    path('api/', include("reviewer.api.urls")),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('process-payment/', views.payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
]

