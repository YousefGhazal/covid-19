from django.db import models
from solo.models import SingletonModel
from ordered_model.models import OrderedModel

# Create your models here.
class Section(OrderedModel, SingletonModel):
    title = models.CharField(max_length=50, blank=False)
    subheading = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
