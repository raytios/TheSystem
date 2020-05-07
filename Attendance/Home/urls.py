"""Attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include,re_path
from . import views

app_name ='home'



urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('<int:employee_id>/', views.details, name='details'),
    re_path(r'^checks/$', views.checks, name='checks'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('<int:employee_id>/create_check/', views.create_check, name='create_check'),
    path('<int:employee_id>/delete_check/<int:check_id>/', views.delete_check, name='delete_check'),
    path('<int:employee_id>/delete_employee/', views.delete_employee, name='delete_employee'),
]
