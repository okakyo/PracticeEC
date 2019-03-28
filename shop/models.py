from django.db import models

# Create your models here.
"""
The Data models 
    Name       : The name of Item
    thubnail   : The picture of Item 
    Value      : The costs of Item
    Explain    : The Explaination of the Item
    Date       : The DateTime of First Posts
    DateExs    : The Datetime of Item 
"""
class ShopItems(models.Model):
    itemName=models.CharField(max_length=100)
    itemValue=models.IntegerField()
    itemExplain=models.TextField(max_length=1000)
    itemDate=models.DateTimeField()
    
    def __str__(self):
        return self.itemName

class ItemThubnail(models.Model):
    picID=models.IntegerField()
    picName=models.CharField(max_length=50)
    picFile=models.ImageField()
    
    def __str__(self):
        return self.picName

class Tag(models.Model):
    tagID=models.IntegerField()
    tagName=models.CharField(max_length=50)

    def __str__(self):
        return self.tagName
