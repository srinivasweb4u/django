from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.


class celebrity(models.Model):
    celebrity_name = models.CharField(max_length=10)
    celebrity_price = models.CharField(max_length=5)
    celebrity_tag = models.CharField(max_length=20)    
    description = models.CharField(max_length=100)
    celebrity_image = models.ImageField(upload_to ='uploads/')
    def __srt__(self):
        return self
      
class bookings(models.Model):
    Name = models.CharField(max_length=40)
    Occasion = models.CharField(max_length=50)
    Video_date = models.DateField()
    To = models.CharField(max_length=50)
    def __srt__(self):
        return self
class author(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=19)

class book(models.Model):
    title = models.CharField(max_length=20)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(author,related_name='book',on_delete=models.CASCADE)

