from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Machine(models.Model):
    hostname = models.CharField(max_length=50)
    ref_url  = models.URLField()
    arch     = models.CharField(max_length=50)
    os       = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    status   = models.CharField(max_length=20)
    note     = models.TextField()
    user     = models.ForeignKey(User)

    def __unicode__(self):
        return self.hostname
