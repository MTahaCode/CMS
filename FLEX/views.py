from django.shortcuts import render,HttpResponse, redirect
from .models import Student
from django.contrib.auth.models import User

def spf(request):
    return render(request, 'spf.html')

def find_UserName(request):
    if request.method == 'POST':
        rollno = request.POST.get('name')
        Password = request.POST.get('password')
        
        if rollno == "admin":
             if Password == "adminadmin":
                return redirect('/admin')

        student = Student.objects.filter(RollNo=rollno, password=Password) 
        if student.exists():
            context = {
                        #this will take a student thing as well
                        'RollNo' : rollno
                    }
            return render(request, 'homepage.html', context)     
        else:
            return index(request)
        # if rollno == "admin":
        #     if password == "adminadmin":
        #         return redirect('/admin')
        # for AStudent in students:
        #     if AStudent.RollNo == rollno:
        #         if AStudent.password == password:
        #             return render(request,'homepage.html')
        #         else:
        #             return index(request)
        # return index(request)
    else:
        return HttpResponse('Invalid request type.')

def index(request):
    return render(request,'loginAndReg.html')

def profile(request):
    
    return render(request,'spf.html')
    #return HttpResponse("WOW")