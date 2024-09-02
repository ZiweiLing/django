from django.shortcuts import render, HttpResponse, redirect
from student.models import Student
from employee.models import Employee

# Create your views here.
def studentInfo(request):
    # GET all employee/user information from models.py, need to import
    data_list = Student.objects.all()
    print(data_list)
    return render(request, 'info.html', {'data_list': data_list})


def studentInfoAdd(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')
    
    # get data written by employees
    studentName = request.POST.get("studentName")
    education = request.POST.get("education")
    university = request.POST.get("university")
    grades = request.POST.get("grades")
    contractStatus = request.POST.get("contractStatus")
    contractTime = request.POST.get("contractTime")

    # add data to MySQL
    Student.objects.create(studentName=studentName, education=education, university=university, grades=grades, contractStatus=contractStatus, contractTime=contractTime)

    # once add successfully, jump to show student info
    return redirect("http://127.0.0.1:8000/student/info/")


def studentInfoDel(request):
    nid = request.GET.get('nid')
    Student.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/student/info/")

