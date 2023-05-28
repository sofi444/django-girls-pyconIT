from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # name of class == name of model
    author = models.ForeignKey( #link to another model
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField() # no length limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #call __string__() and get title
        return self.title