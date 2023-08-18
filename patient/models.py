from django.db import models

# Create your models here.
class Patient(models.Model):
    sex=(("Male","Male") ,
    ( "Female","Female",))
    

    p_name=models.CharField(max_length=50)
    p_age=models.CharField(max_length=50)
    p_phone=models.CharField(max_length=20)
    p_sex=models.CharField(choices=sex,max_length=20)
