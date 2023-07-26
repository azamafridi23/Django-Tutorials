'''
In Django, the models.py file is used to define the database structure and behavior of your application. 
It is a Python module that contains the Django model classes, which represent database tables.

'''

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model): # Each class will be its own table in the database
    title = models.CharField(max_length=100) # These are my fields
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk}) 


