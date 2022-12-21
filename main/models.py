from django.db import models
from solo.models import SingletonModel
from ordered_model.models import OrderedModel

# Create your models here.
class Announcements(OrderedModel):
    title = models.CharField(max_length=50, blank=False)
    subheading = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Heading(SingletonModel):
    header = models.CharField(max_length=255, default='header')
    subheader = models.CharField(max_length=300, default='subheader')

    def __str__(self):
            return self.header