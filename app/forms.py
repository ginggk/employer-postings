from django import forms


class JobForm(forms.Form):
    company = forms.CharField()
    job_title = forms.CharField()
    location = forms.CharField()
    job_function = forms.CharField()
    employment_type = forms.CharField()
    company_industry = forms.CharField()
    seniority_level = forms.CharField()
    job_description = forms.CharField()
    logo = forms.URLField()
