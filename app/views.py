from django.shortcuts import render, redirect
from django.views import View
# from app import forms
from . import models

# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'home.html')
