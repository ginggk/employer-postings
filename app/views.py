from django.shortcuts import render, redirect
from django.views import View
from app import forms
from . import models

# Create your views here.


class Home(View):
    def get(self, request):

        return render(request, 'home.html',
                      {'JobForm': models.Posting.objects.all()})


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
            models.Posting.submitted(
                company, job_title, location, job_function, employment_type,
                company_industry, seniority_level, job_description, logo)
            return redirect('home')
        else:
            return render(request, 'job.html', {'JobForm': form})


class PostingDetails(View):
    def get(self, request, id):
        return render(request, 'details.html',
                      {'JobForm': models.Posting.objects.get(id=id)})


class ShowEmployers(View):
    def get(self, request):
        # print(models.Posting.objects.values())
        return render(
            request, 'employers.html', {
                'employers':
                models.Posting.objects.values('company', 'logo').distinct()
            })
