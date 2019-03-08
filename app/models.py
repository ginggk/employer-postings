from django.db import models

# Create your models here.


class Posting(models.Model):
    company = models.TextField()
    job_title = models.TextField()
    location = models.TextField()
    job_function = models.TextField()
    employment_type = models.TextField()
    company_industry = models.TextField()
    seniority_level = models.TextField()
    job_description = models.TextField()
    logo = models.URLField()


@staticmethod
def submitted(company, job_title, location, job_function, employment_type,
              company_industry, seniority_level, job_description, logo):
    Posting(
        company=company,
        job_title=job_title,
        location=location,
        job_function=job_function,
        employment_type=employment_type,
        company_industry=company_industry,
        seniority_level=seniority_level,
        job_description=job_description,
        logo=logo).save()
