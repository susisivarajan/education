from django.db import models
class student(models.Model):
    name=models.CharField(max_length=150,null=True)
    dob=models.DateField(null=True)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=150,null=True)
    phonenumber=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    address=models.TextField(null=True)
    department= models.CharField(max_length=20, null=True)
    purpose=models.CharField(max_length=20,null=True)
    materialsprovided=models.CharField(max_length=20,null=True)
    class Meta:
        verbose_name_plural='student'
