from django.db import models

# Create your models here.
class sellers(models.Model):
        seller_id = models.CharField(max_length=200)
        first_name = models.CharField(max_length=200)
        last_name = models.CharField(max_length=200)
        picture = models.TextField()
        phone = models.IntegerField()
        email = models.EmailField()
        size = models.IntegerField()
        address = models.TextField()
        description = models.TextField()
        video = models.TextField()
        timings = models.TextField()

        def __str__(self):
            return (self.first_name + self.last_name)
            
class sellers(models.Model):
        seller_id = models.CharField(max_length=200)
        first_name = models.CharField(max_length=200)
        last_name = models.CharField(max_length=200)
        picture = models.TextField()
        phone = models.IntegerField()
        email = models.EmailField()
        size = models.IntegerField()
        address = models.TextField()
        description = models.TextField()
        video = models.TextField()
        timings = models.TextField()

        def __str__(self):
            return (self.first_name + self.last_name)
        
