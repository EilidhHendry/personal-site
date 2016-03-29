from django.db import models
from time import strftime

class Project(models.Model):
    title = models.CharField(max_length = 100)
    summary = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)
    technologies = models.TextField()

    def __unicode__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    summary = models.TextField()

    def __unicode__(self):
        return self.degree

class Job(models.Model):
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    description = models.TextField()
    technologies = models.TextField()

    def __unicode__(self):
        return " ".join([self.company, self.job_title])

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    location = models.CharField(max_length=100)

    def full_name(self):
        return " ".join([self.first_name, self.last_name])

    def __unicode__(self):
        return self.full_name()

class Overview(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return self.text[0:20]
