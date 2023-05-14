from django.shortcuts import render
from .models import Announcements, Teacher
# Create your views here.


def index(request):
    announcements = Announcements.objects.all()

    data = {
        'page': 'Announcements',
        'announcements': announcements,
        'username': "Ahmed Ali"
    }
    return render(request, 'announcements.html', data)


def delete_announcement(request):
    print(request.POST.get('id'))
    if request.method == 'POST':
        if request.POST.get('id') == None:
            announcements = Announcements.objects.all()
            data = {
                'page': 'Announcements',
                'announcements': announcements,
                'username': "Ahmed Ali"
            }

            return render(request, 'announcements.html', data)

        id = request.POST.get('id')
        announcement = Announcements.objects.get(id=id)
        announcement.delete()

        announcements = Announcements.objects.all()
        data = {
            'page': 'Announcements',
            'announcements': announcements,
            'username': "Ahmed Ali"
        }

        return render(request, 'announcements.html', data)


def add_announcement(request):
    if request.method == 'POST':
        if request.POST.get('announcement') == '' or request.POST.get('teachername') == '':
            announcements = Announcements.objects.all()
            data = {
                'page': 'Announcements',
                'announcements': announcements,
                'username': "Ahmed Ali"
            }

            return render(request, 'announcements.html', data)

        announcement = request.POST.get('announcement')
        teachername = request.POST.get('teachername')

        teacher = Teacher.objects.get(Name=teachername)

        announcement = Announcements(
            announcement=announcement, teacher=teacher)

        announcement.save()

        announcements = Announcements.objects.all()

        data = {
            'page': 'Announcements',
            'announcements': announcements,
            'username': "Ahmed Ali"
        }

        # add announcement
        return render(request, 'announcements.html', data)
