from django.contrib import admin
from Attendance.models import Student, Attendance, Date

# Register your models here.
admin.site.register(Student)
admin.site.register(Date)
admin.site.register(Attendance)