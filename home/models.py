from django.db import models
from datetime import date

class Project(models.Model):
    title = models.CharField(max_length = 100)
    summary = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)
    technologies = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.TextField()

class Job(models.Model):
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    technologies = models.TextField()
