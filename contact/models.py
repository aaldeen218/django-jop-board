from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.TextField(max_length=5000)