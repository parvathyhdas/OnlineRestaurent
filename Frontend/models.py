from django.db import models

# Create your models here.
class ReservationDB(models.Model):
    Date = models.DateField(max_length=30,null=True,blank=True)
    Time =models.CharField(max_length=30,null=True,blank=True)
    People =models.CharField(max_length=30,null=True,blank=True)
    Name =models.CharField(max_length=30,null=True,blank=True)
    Phone =models.CharField(max_length=30,null=True,blank=True)
    Email =models.EmailField(max_length=30,null=True,blank=True)

class RegisterDB(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=30, null=True, blank=True)
    UserName = models.CharField(max_length=30, null=True, blank=True)
    Password = models.CharField(max_length=30, null=True, blank=True)


class ContactDB(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=30, null=True, blank=True)
    Phone = models.CharField(max_length=30, null=True, blank=True)
    Message = models.CharField(max_length=30, null=True, blank=True)
