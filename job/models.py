from django.db import models

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
 )
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)  
    
    def __str__(self):
        return self.name  

class Job(models.Model):
    title=models.CharField(max_length=50)
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey(Category,related_name='job_catogrey',on_delete=models.CASCADE)
    #image=models.ImageField(upload_to='jops/')


    def __str__(self):
        return self.title
    
