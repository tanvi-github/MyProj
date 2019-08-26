from django.db import models

# Create your models here.
# Web1 is the name of class and so will be the the name of the table
class web1(models.Model):
    news_head=models.CharField(max_length=255) #attribute1 of table web1
    news_web=models.CharField(max_length=255)  #attribute2 of table web1
    date=models.DateField()    #attribute3 of table web1

class News(models.Model):
    title=models.CharField(max_length=225)
    authors=models.CharField(max_length=225)
    publisher=models.ForeignKey(web1,on_delete=models.PROTECT)
    publication_date=models.DateField()

class tb_Registration(models.Model):
    name=models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

class basic(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)

class employee(models.Model):
    name=models.CharField(max_length=30)
    salary=models.IntegerField()
    job_title=models.CharField(max_length=30)
    details=models.CharField(max_length=30)

