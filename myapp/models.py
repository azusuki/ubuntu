from django.db import models

# Create your models here
class Area(models.Model):
     number = models.IntegerField()
     area = models.CharField(max_length = 100)
     cityname = models.CharField(max_length = 100)

     def __str__(self):
         return str(self.number)

class Category(models.Model):
    is_check = models.BooleanField(default=False, verbose_name="表示フラグ")
    title = models.CharField(max_length=100)
    title_num = models.IntegerField()
    foreign_number = models.ForeignKey(Area, on_delete= models.SET_NULL,null=True)

    def __str__(self):
        return str(self.title)
