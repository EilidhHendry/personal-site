from django.db import models
from datetime import date

class Project(models.Model):
    title = models.CharField(max_length = 100)
    summary = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField(default=date.today)
    link = models.URLField(blank=True)

    def __unicode__(self):
        return self.title
