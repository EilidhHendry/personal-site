from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    published_date = models.DateTimeField()
    text = models.TextField()

    def __unicode__(self):
        return self.title


