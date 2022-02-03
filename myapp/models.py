from django.db import models

# Create your models here
class Area(models.Model):
     number = models.IntegerField()
     area = models.CharField(max_length = 100)
     cityname = models.CharField(max_length = 100)

     def __str__(self):
         return str(self.number)
