from django.db import models

# Create your models here.
class logindata(models.Model):
    Name = models.CharField(max_length=150)
    Education = models.CharField(max_length=150)
    Phone_no = models.CharField(max_length=150)
    City = models.CharField(max_length=150)
    Password = models.CharField(max_length=128) 
    Email = models.EmailField(unique=True) 


    class meta:
        db_table = 'login'

class contactdata(models.Model):
    ptname = models.CharField(max_length= 20)
    department = models.CharField(max_length= 20)
    medicine = models.CharField(max_length= 20)
    city = models.TextField()
    Email = models.EmailField()
    
    class meta:
        db_table = 'test'  


  

