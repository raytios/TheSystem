from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.


class Employee(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,)
    employee_no = models.IntegerField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    is_choose = models.BooleanField(default =False)
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
class Check(models.Model):
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    time_in = models.TimeField()
    time_out = models.TimeField()
    is_choose = models.BooleanField(default =False)

    def __str__(self):
        return str(self.time_in) + ' - ' + str(self.time_out) 

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
