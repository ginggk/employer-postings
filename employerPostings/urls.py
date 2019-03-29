"""employerPostings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('jobs/', views.Job.as_view(), name='job'),
    path('details/<int:id>', views.PostingDetails.as_view(), name='details'),
    path('employers/', views.ShowEmployers.as_view(), name='employers'),
    path('resources/', views.ShowResources.as_view(), name='resources'),
    path('comment/<int:id>', views.ShowComments.as_view(), name='comments'),
    path('admin/', views.AdminPage.as_view(), name='admin'),
    path(
        'jobs/<int:id>/delete', views.DeletePost.as_view(), name='delete-job'),
    # path('search/', views.Search.as_view(), name='search')
]
