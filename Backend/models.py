from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="Images",null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)

class ItemDB(models.Model):
    ItemCategory = models.CharField(max_length=100,null=True,blank=True)
    ItemName = models.CharField(max_length=100,null=True,blank=True)
    ItemPrice = models.IntegerField(null=True,blank=True)
    ItemImage = models.ImageField(upload_to="ItemImages",null=True,blank=True)
    ItemDescription = models.CharField(max_length=100,null=True,blank=True)