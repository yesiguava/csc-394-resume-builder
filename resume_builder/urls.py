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
from django.urls import path
from resume_builder.views import qualifications,index,about,contact,signin,output_view,submit_form


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
    path('index.html', index),
    path('about.html', about),
    path('qualifications.html', qualifications),
    path('contact.html', contact),
    path('signin.html', signin),
    path('output/', output_view, name='output-name'),
    path('submit/', submit_form)
]
