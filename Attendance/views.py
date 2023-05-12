from django.shortcuts import render , HttpResponse
from datetime import date
import datetime
from .models import Student, Date, Attendance
import json

def delete_attendance_of_one_date(request):
    if request.method == 'POST':
        Date_To_Delete_str = request.POST.get('DateToBeDeleted')
        Date_To_Delete = datetime.datetime.strptime(Date_To_Delete_str, "%B %d, %Y").date()
        print(Date_To_Delete)
        dateFromModel = Date.objects.filter(date=Date_To_Delete).first()
        if dateFromModel:
            print("date exists")
            print(dateFromModel)
            dateFromModel.delete()
        else:
            print("date does not exist")
            
        return HttpResponse('New Attendance data received successfully.')
    else:
        return HttpResponseBadRequest('Invalid request type.')

def add_New_Attendance(request):
    if request.method == 'POST':
        new_date_str = request.POST.get('new_date')
        new_date = datetime.datetime.strptime(new_date_str, "%B %d, %Y").date()
        students = Student.objects.all() 
        dates = Date.objects.all()
        for aStudent in students:
            for aDate in dates:
                aAttendance = Attendance.objects.filter(student=aStudent, date=aDate).first()
                if aAttendance is None:
                    attendance = Attendance.objects.create(date=aDate, student=aStudent, attendance="--")
                    attendance.save()
        return HttpResponse('New Attendance data received successfully.')
    else:
        return HttpResponseBadRequest('Invalid request type.')

def add_New_Date(request):
    print("add a new date function called")
    if request.method == 'POST':
        new_date_str = request.POST.get('new_date')
        new_date = datetime.datetime.strptime(new_date_str, "%B %d, %Y").date()
        New_Date = Date.objects.create(date=new_date)
        New_Date.save()
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
        if attendance_str:
            attendance = json.loads(attendance_str)
        else:
            attendance = []

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
                else:
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
    context = {
        #this will take a student thing as well
        'dates' : dates,
        'rows': rows,
        'date': date.today()
    }
    return render(request, 'attendance_page.html', context)

def another(request):
    return HttpResponse('this is another function')