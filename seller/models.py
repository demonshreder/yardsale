from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
        docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class UserProfile(models.Model):
        # This line is required. Links UserProfile to a User model instance.
        user_boy = models.OneToOneField(User, default=uuid.uuid4)
        # Additional Attributes
        picture = models.URLField(blank=True)
        phone = models.CharField(max_length=12,blank=True)
        address = models.TextField(blank=True)
        desc = models.TextField()
        video = models.URLField(blank=True)
        timings = models.CharField(max_length=200)

        def __str__(self):
            return (self.desc)

            
class products(models.Model):
        seller = models.ForeignKey(User, default=uuid.uuid4)
        product_name = models.CharField(max_length=200)
        age = models.CharField(max_length=50)
        reason = models.TextField()
        listed = models.DateField()
        sold = models.BooleanField()
        video = models.URLField()
        picture = models.ImageField(upload_to="product_images",default = 'static/img/placeholder.jpg')
        desc = models.TextField()

        def __str__(self):
            return (self.product_name)
        
