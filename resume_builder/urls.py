"""
URL configuration for resume_builder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from resume_builder.views import (
    index_view,
    about_view,
    qualifications_view,
    contact_view,
    signin_view,
    output_view,
    submit_form
)
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index_view, name='index'),
    path('index.html', index_view, name='index'),
    path('about.html', about_view, name='about'),
    path('qualifications.html', qualifications_view, name='qualifications'),
    path('contact.html', contact_view, name='contact'),
    path('signin.html', signin_view, name='signin'),
    path('output/', output_view, name='output-name'),
    path('submit/', submit_form, name='submit_form'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login')
]
