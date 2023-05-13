from django.shortcuts import render,HttpResponse, redirect
from .models import Student
from django.contrib.auth.models import User

def spf(request):
    return render(request, 'spf.html')

def find_UserName(request):
    if request.method == 'POST':
        return redirect('Attenance:attendance')
        # rollno = request.POST.get('RollNo')
        # password = request.POST.get('Password')
        # print(request.POST.get('RollNo'))
        # print(request.POST.get('Password'))
        # students = Student.objects.all() 
        # print(students)
        # for AStudent in students:
        #     print(AStudent.RollNo)
        #     print(AStudent.password)
        #     if AStudent.RollNo == rollno:
        #         print('inside the single if')
        #         if AStudent.password == password:
        #             print('inside the double if')
        #             return render(request,'spf.html')
        #         else:
        #             return render(request,'loginAndReg.html')
        # return HttpResponse('Success')
    else:
        return HttpResponse('Invalid request type.')

def index(request):
    return render(request,'loginAndReg.html')

def profile(request):
    
    return render(request,'spf.html')
    #return HttpResponse("WOW")