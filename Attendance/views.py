from django.shortcuts import render , HttpResponse
from datetime import date
from .models import Student, Date, Attendance
import json

def add_New_Date(request):
    if request.method == 'POST':
        new_date_str = request.POST.get('date')
        new_date = datetime.strptime(new_date_str, '%Y-%m-%d').date()
        NewDate = Date.objects.create(date=new_date)
        NewDate.save()
        return HttpResponse('Attendance data received successfully.')
    else:
        return HttpResponseBadRequest('Invalid request type.')

def save_attendance(request):
    print("save_attendance function called!")
    students = Student.objects.all() 
    dates = Date.objects.all()
    if request.method == 'POST':
        # retrieve the attendance data
        attendance_str = request.POST.get('attendance')
        attendance = json.loads(attendance_str)
        #for aStudent in students:
        #for aDate in dates:

        # for row in attendance:
        #     for cell in row:

        for row,aStudent in zip(attendance,students):
            for cell,aDate in zip(row,dates):
                aAttendance = Attendance.objects.filter(student=aStudent, date=aDate).first()
                if not aAttendance:
                    aAttendance = Attendance(student=aStudent, date=aDate, attendance='')
                if cell == "absent":
                    aAttendance.attendance = 'A'
                elif cell == "present":
                    aAttendance.attendance = 'P'
                elif cell == "late":
                    aAttendance.attendance = 'L'
                elif cell == "--":
                    aAttendance.attendance = ""
                aAttendance.save()

        for row,aStudent in zip(attendance,students):
            for cell,aDate in zip(row,dates):
                aAttendance = Attendance.objects.filter(student=aStudent, date=aDate).first()
                if aAttendance is None:
                    attendance = Attendance.objects.create(date=aDate, student=aStudent, attendance="--")
                if cell == "absent":
                    print(cell)
                    aAttendance.attendance = 'A'
                elif cell == "present":
                    print(cell)
                    aAttendance.attendance = 'P'
                elif cell == "late":
                    print(cell)
                    aAttendance.attendance = 'L'
                elif cell == "--":
                    print(cell)
                    aAttendance.attendance = "--"
                aAttendance.save()
                print(aDate.date,aStudent.Name)
                    #print(cell,aStudent,aDate)
        # retrieve the date
        #date = request.POST.get('date')
        # do something with the attendance and date data
        return HttpResponse('Attendance data received successfully.')
    else:
        return HttpResponseBadRequest('Invalid request type.')

    return render(request, 'attendance.html', {'students': students})

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
            # if aAttendance is None:
            #     AttendanceForOneStudent.append('None')
            # else:
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
        'date': date.today()
    }
    return render(request, 'attendance_page.html', context)

def another(request):
    return HttpResponse('this is another function')