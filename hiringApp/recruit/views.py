from django.shortcuts import render, redirect
from .models import Response
import fileinput
import sys
from subprocess import run, PIPE
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
        global out
        print(responsibilities, t_skills, s_skills)
        t = 'C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/text files/recruit/Sample CV text.txt'
        for lines in fileinput.FileInput(t, inplace=1):
            if 'Responsibilities:' in lines:
                lines = lines[:17]
                lines = lines.replace(lines, lines + '\n' + responsibilities)
            print(lines, end='')
        for lines in fileinput.FileInput(t, inplace=1):
            if 'Technical skills:' in lines:
                lines = lines[:17]
                lines = lines.replace(lines, lines + '\n' + t_skills)
            print(lines, end='')
        for lines in fileinput.FileInput(t, inplace=1):
            if 'Soft skills:' in lines:
                lines = lines[:12]
                lines = lines.replace(lines, lines + '\n' + s_skills)
            print(lines, end='')
        ins = Response(responsibilities=responsibilities, tech_skills=t_skills, soft_skills=s_skills)
        ins.save()
        out = run([sys.executable, 'C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/comparisons.py'], shell=False, stdout=PIPE)
        return redirect('success')
    print("The data has been written to the db")
    return render(request, 'home.html')


def success(request):
    if request.method == "POST":
        return redirect('response')
    return render(request, 'success.html')


def response(request):
    if request.method == "POST":
        ssw = open('C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/text files/recruit/Sample CV text.txt', 'w+')
        liner = 'Responsibilities:' + '\n' + '\n' 'Technical skills:' + '\n' + '\n' 'Soft skills:'
        ssw.write(liner)
        print(out)
        return redirect('index')
    return render(request, 'response.html', {'result': out.stdout.decode('utf-8')})
