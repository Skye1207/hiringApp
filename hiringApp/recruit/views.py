from django.shortcuts import render, redirect
from .models import Response
import fileinput

# Create your views here.


def index(request):
    return render(request, 'base.html')


def home(request):
    if request.method == "POST":
        global responsibilities
        responsibilities = request.POST['R']
        global t_skills
        t_skills = request.POST['T']
        global s_skills
        s_skills = request.POST['S']
        # print(responsibilities, t_skills, s_skills)
        ins = Response(responsibilities=responsibilities, tech_skills=t_skills, soft_skills=s_skills)
        ins.save()
        return redirect('success')
    f = 'C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/static/recruit/Sample CV text.txt'
    for line in fileinput.FileInput(f, inplace=1):
        if 'Responsibilities:' in line:
            line = line.rstrip()
            line = line.replace(line, line + 'responsibilities.objects.all' + '\n')
        print(line, end='')
    for line in fileinput.FileInput(f, inplace=1):
        if 'Technical skills:' in line:
            line = line.rstrip()
            line = line.replace(line, line + 't_skills.objects.all' + '\n')
        print(line, end='')
    for line in fileinput.FileInput(f, inplace=1):
        if 'Soft skills:' in line:
            line = line.rstrip()
            line = line.replace(line, line + 's_skills.objects.all' + '\n')
        print(line, end='')
    print("The data has been written to the db")
    return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')
