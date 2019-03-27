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


