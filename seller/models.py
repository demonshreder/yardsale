from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
        docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class UserProfile(models.Model):
        # This line is required. Links UserProfile to a User model instance.
        user = models.OneToOneField(User)
        # Additional Attributes
        picture = models.URLField(blank=True)
        phone = models.CharField(max_length=12,blank=True)
        address = models.TextField(blank=True)
        desc = models.TextField()
        video = models.URLField(blank=True)
        timings = models.TextField()

        def __unicode__(self):
            return self.user.username

            
class products(models.Model):
        seller = models.OneToOneField(User)
        product_name = models.CharField(max_length=200)
        age = models.IntegerField()
        reason = models.TextField()
        listed = models.DateField()
        sold = models.BooleanField()
        video = models.TextField()
        picture = models.TextField()
        desc = models.TextField()

        def __str__(self):
            return (self.product_name)
        
