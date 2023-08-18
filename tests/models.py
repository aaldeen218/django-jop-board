from django.db import models

# Create your models here.

class Test(models.Model):
    test_name=models.CharField(max_length=50)
    test_short_name=models.CharField(max_length=50)
    test_price=models.IntegerField()

    def __str__(self):
        return self.test_name

class SubTest(models.Model):
    
    test_name=models.ForeignKey(Test,max_length=50,default=1,related_name='Test_name',on_delete=models.CASCADE)
    sub_name=models.CharField(max_length=50)
    sub_normal=models.CharField(max_length=50)
    sub_part=models.IntegerField()
    
    

    def __str__(self):
        return self.sub_name
    


