from django.db import models

# Create your models here.


class Teacher(models.Model):
    Name = models.CharField(max_length=150)
    PfpUrl = models.CharField(max_length=150)


class Announcements(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    announcement = models.CharField(max_length=512)
