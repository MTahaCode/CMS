from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=150)
    RollNo = models.CharField(max_length=150)
    # Attendance = models.CharField(max_length=10)

class Date(models.Model):
    date = models.DateField()

class Attendance(models.Model):
    #have to create a attendance column according to the number of students
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance = models.CharField(max_length=1)
    