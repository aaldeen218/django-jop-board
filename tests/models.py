from django.utils import timezone
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import *

# Create your models here.

class Test(models.Model):
    test_name=models.CharField(max_length=50)
    test_price=models.IntegerField()

    def __str__(self):
        return self.test_name

class SubTest(models.Model):
    
    test_name=models.ForeignKey(Test,max_length=50,default=1,related_name='Test_name',on_delete=models.CASCADE)
    sub_name=models.CharField(max_length=50)
    sub_normal=models.CharField(max_length=50,null=True,blank=True)
    sub_part=models.IntegerField(blank=True,null=True)

        
    def __str__(self):
        return  self.sub_name
    


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
    check_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    created= models.DateTimeField(editable=False,null=True,blank=True)
    modified= models.DateTimeField(null=True,blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Check, self).save(*args, **kwargs)    
    
    def __str__(self):
        #return  f'{self.p_name} # {self.id},'
        return    str(self.p_name)+"#"+str(self.id)+"|"+"|".join(self.test_name.all().values_list('test_name', flat=True))



class Check_items(models.Model):
    check_id=models.ForeignKey(Check,max_length=1000, on_delete= models.DO_NOTHING)
    sub_id=models.ForeignKey(SubTest,max_length=50, on_delete= models.DO_NOTHING,null=True,blank=True)
    check_result=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return str(self.check_id)
        

@receiver(m2m_changed, sender=Check.test_name.through)
def update_counter(sender, instance, action, reverse, model, pk_set, **kwargs):
   
    if action == "post_add":
        print(5555)
        print(instance)
        # مفتاح الربط قبل مسح الرقم واسم المريض منه بغرض الحصول على الفحصوات الفرعية
        instance_2=instance 
        
         # مسح جميع الفحوصات الفرعية في بداية كل عملية انشاء او تعديل لحماية البيانات من التكرار
        Check_items.objects.filter(check_id=instance_2).delete()
        t=Test.objects.all()
        l=[]
        l=str(instance).split("|")
        l.pop(0)
        
        temp=[]
        for i in t:
            #print(i)
            for cc in l:
              #print(cc)
              if i.test_name==cc:
                  temp.append(i.id)

        
        
        s=SubTest.objects.filter(test_name__in=temp)
        #print(l)

        
        #print(s)
        for x in s:
            print(x)
            Check_items.objects.create(check_id=instance_2,sub_id=x)





        # for x in s:
        #   for ll in l:
        #     if x.test_name == ll:
        #        temp.append(x.test)
        #print(temp)       
        #     if x.test_name in instance:
        #        print(x.sub_name ) 
        
        #instance.save()    

# @receiver(post_save,sender=Check)  
# def create_user_profile(sender,instance,created,**kwargs):
    
    
#     print("44444444444")
#     print(instance)

#     if created:
#         Check_items.objects.create(check_id=instance,sub_id=SubTest.objects.get(id=26))
