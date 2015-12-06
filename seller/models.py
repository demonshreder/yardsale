from django.db import models

# Create your models here.

class Document(models.Model):
        docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class sellers(models.Model):
        first_name = models.CharField(max_length=200)
        last_name = models.CharField(max_length=200)
        docfile = models.FileField(upload_to='documents/%Y/%m/%d')
        phone = models.IntegerField()
        email = models.EmailField()
        address = models.TextField()
        desc = models.TextField()
        video = models.TextField()
        timings = models.TextField()

        def __str__(self):
            return (self.first_name + self.last_name)
            
class products(models.Model):
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
        
