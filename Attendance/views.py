from django.shortcuts import render , HttpResponse
from datetime import date
from .models import Student, Date, Attendance

def my_function():
    return "Hello, world!"
    


def main(request):
    students = Student.objects.all() 
    dates = Date.objects.all()
    rows = []
    serialNo=0
    for aStudent in students:
        serialNo += 1
        AttendanceForOneStudent = []
        for aDate in dates:
            aAttendance = Attendance.objects.filter(student=aStudent, date=aDate).first()
            if aAttendance is None:
                AttendanceForOneStudent.append('None')
            else:
                AttendanceForOneStudent.append(aAttendance.attendance)
        aRow = {
                'SNo': serialNo,
                'name': aStudent.Name,
                'rollNo': aStudent.RollNo,
                'attendanceList' : AttendanceForOneStudent,
        }
        rows.append(aRow)
    # rows = [
    #     {'name':'Taha','rollNo':'i221547','attendance':'present'},
    #     {'name':'Affan','rollNo':'i222603','attendance':'present'},
    #     {'name':'Sami','rollNo':'i22717','attendance':'present'},
    #     {'name':'Sami','rollNo':'i22717','attendance':'present'},
    # ]

    context = {
        #this will take a student thing as well
        'dates' : dates,
        'rows': rows,
    }
    return render(request, 'attendance_page.html', context)

def another(request):
    return HttpResponse('this is another function')