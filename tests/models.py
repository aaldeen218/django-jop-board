from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Test(models.Model):
    test_name=models.CharField(max_length=50)
    test_price=models.IntegerField()

    def __str__(self):
        return self.test_name

class SubTest(models.Model):
    
    test_name=models.ForeignKey(Test,max_length=50,default=1,related_name='Test_name',on_delete=models.CASCADE)
    sub_name=models.CharField(max_length=50)
    sub_normal=models.CharField(max_length=50)
    sub_part=models.IntegerField(blank=True,null=True)
    
    

    def __str__(self):
        return self.sub_name
    

class Patient(models.Model):
    SEX_TYPE=(
    ('Male','Male'),
    ('Female','Female'),)
    
    p_name=models.CharField(max_length=50,verbose_name='Patient Name',unique=True)
    p_sex=models.CharField(max_length=50,choices=SEX_TYPE,default=1,verbose_name='Sex')
    p_age=models.IntegerField(null=True,blank=True,verbose_name='Age')
    p_phone=models.CharField(max_length=15, null=True,blank=True,verbose_name='Phone')
    
    def __str__(self):
        return self.p_name
    

class Check(models.Model):  
    p_name=models.ForeignKey(Patient,max_length=50,default=1,related_name='p_check',on_delete=models.CASCADE)
    test_name=models.ManyToManyField(Test,related_name='check_test',blank=False)
    check_total=models.IntegerField(null=True,blank=True)
    check_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  f'{self.p_name} # {self.id}'
  
    

# @receiver(post_save,sender=Check)  
# def create_user_profile(sender,instance,created,**kwargs):
#     print(instance)
#     if created:
#         Patient.objects.create(p_name='aaa',p_sex=1)
