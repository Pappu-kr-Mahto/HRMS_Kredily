from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100,null=False)
    email=models.CharField(max_length=100,null=False)
    department=models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    doj=models.CharField(max_length=30)
    attendance=models.TextField(default=[])
    isactive=models.IntegerField(default=1)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    