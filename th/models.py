from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)


class Club(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='RegistrationReceipt')


class RegistrationReceipt(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    paid_dues = models.BooleanField(default = True)
    fee_payment_date = models.DateTimeField() 