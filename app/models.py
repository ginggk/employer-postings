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
    def submit_post(company, job_title, location, job_function,
                    employment_type, company_industry, seniority_level,
                    job_description, logo):
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

    def __str__(self):
        return '''
            Company Name: {}
            Job Title: {}
            Job Location: {}
            Employment Type: {}
            Seniority Level: {}
            Job Description: {}
            '''.format(self.company, self.job_title, self.location,
                       self.employment_type, self.seniority_level,
                       self.job_description, self.logo)


class Comment(models.Model):
    name = models.TextField()
    comment = models.TextField()
    post_comment = models.ForeignKey(Posting, on_delete=models.PROTECT)

    def __str__(self):
        return '''
            Name: {}
            Comment: {}
            '''.format(self.name, self.comment, self.post_comment)

    @staticmethod
    def submit_comment(name, comment, post_comment_id):
        Comment(
            name=name, comment=comment,
            post_comment_id=post_comment_id).save()
