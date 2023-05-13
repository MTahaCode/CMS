from django.db import models

class Student(models.Model):
    RollNo = models.CharField(max_length=150, default='')
    password = models.CharField(max_length=150)
    # def _str_(self):
    #     return self.RollNo
# Create your models here.
