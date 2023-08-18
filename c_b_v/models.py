from django.db import models

# Create your models here.
class Student(models.Model):
   name= models.CharField( max_length=50)
   address= models.CharField( max_length=50)
   age= models.IntegerField()
   create_at= models.DateTimeField( auto_now_add=True,blank=True,null=True)

   def __str__(self):
      return self.name