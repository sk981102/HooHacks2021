"""debunk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages import views
from survey.views import survey1_view,covid_view,other_view, facts_view
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.home_view, name='home'),
    path('analysis/', views.analysis_view, name='analysis'),
    path('survey/',survey1_view, name='survey1'),
    path('covid/',covid_view, name='covid'),
    path('other/',other_view, name='other'),
    path('facts/',facts_view, name='facts'),
]
