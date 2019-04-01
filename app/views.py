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
            models.Posting.submit_post(
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


class ShowResources(View):
    def get(self, request):
        return render(request, 'resources.html')


class ShowComments(View):
    def get(self, request, id):
        return render(request, 'comments.html',
                      {'comments': forms.CommentForm()})

    def post(self, request, id):
        form = forms.CommentForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            models.Comment.submit_comment(name, comment, id)
            return redirect('home')
        else:
            return render(request, 'comments.html', {'comments': form})


class AdminPage(View):
    def get(self, request):
        return render(request, 'admin.html',
                      {'JobForm': models.Posting.objects.all()})


class DeletePost(View):
    def post(self, request, id):
        models.Posting.objects.get(id=id).delete()
        return redirect('admin')


class AToZ(View):
    def get(self, request):
        return render(
            request, 'az.html', {
                'JobForm':
                models.Posting.objects.all().extra(
                    select={
                        'lower_job_title': 'lower(job_title)'
                    }).order_by('lower_job_title')
            })


class SortByNewestToOldest(View):
    def get(self, request):
        return render(
            request, 'sort-by-newest-to-oldest.html',
            {'JobForm': models.Posting.objects.all().order_by('-date')})


class SortByOldestToNewest(View):
    def get(self, request):
        return render(
            request, 'sort-by-oldest-to-newest.html',
            {'JobForm': models.Posting.objects.all().order_by('date')})


class DeleteComment(View):
    def post(self, request, id):
        models.Comment.objects.get(id=id).delete()
        return redirect('home')
