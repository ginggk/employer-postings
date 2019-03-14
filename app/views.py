from django.shortcuts import render, redirect
from django.views import View
from app import forms
from . import models

# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class Job(View):
    def get(self, request):
        return render(request, 'job.html', {'JobForm': forms.JobForm()})

    def post(self, request):
        form = forms.JobForm(data=request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            job_title = form.cleaned_data['job_title']
            location = form.cleaned_data['location']
            job_function = form.cleaned_data['job_function']
            employment_type = form.cleaned_data['employment_type']
            company_industry = form.cleaned_data['company_industry']
            seniority_level = form.cleaned_data['seniority_level']
            job_description = form.cleaned_data['job_description']
            logo = form.cleaned_data['logo']
            return redirect('home')
        else:
            return render(request, 'job.html', {'JobForm': form})