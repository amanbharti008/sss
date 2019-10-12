from django.db import models
from datetime import datetime,date

class question(models.Model):
    id_1=models.CharField(max_length=100)
    message=models.CharField(max_length=500)
    comment=models.IntegerField(max_length=10)
    updated_date=models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.message

class reviews(models.Model):
    id_2=models.IntegerField(max_length=50)
    body=models.CharField(max_length=500)
    reacts=models.IntegerField(max_length=10)
    

    def __str__(self):
        return self.body      


# Create your models here.
