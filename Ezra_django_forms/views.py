from django.shortcuts import render
from .form import UserReg
from .form import peoplereg
from .form import studentsreg


def Reg(request):
    submit_btn = request.POST.get("register")
    name = ''
    email = ''
    password = ''

    rForm = UserReg(request.POST or None)
    if rForm.is_valid():
        name = rForm.cleaned_data.get("name")
        email = rForm.cleaned_data.get("email")
        password = rForm.cleaned_data.get("password")

    context = {'rForm': rForm, 'name': name, 'email': email, 'submit_btn': submit_btn}
    return render(request, 'register.html', context)


def reg_people(request):
    submit_people_btn = request.POST.get("peoplebtn")
    name = ''
    age = ''
    phone = ''
    city = ''

    people_form = peoplereg(request .POST or None)
    if people_form.is_valid():
         name = people_form.cleaned_data.get("name")
         age = people_form.cleaned_data.get("age")
         phone = people_form.cleaned_data.get("phone")
         city = people_form.cleaned_data.get("city")
    context = {'people_form':people_form,
               'name': name,
               'age': age,
               'phone': phone,
               'city': city,
               'submit_people_btn': submit_people_btn
               }
    return render(request,'people.html', context)

def reg_students(request):
    submit_students_btn = request.POST.get("studentsbtn")
    name = ''
    gender = ''
    school = ''
    parent = ''
    phone_number = ''

    students_form = studentsreg(request.POST or None)
    if students_form.is_valid():
        name = students_form.cleaned_data.get("name")
        gender = students_form.cleaned_data.get("gender")
        school = students_form.cleaned_data.get("school")
        parent = students_form.cleaned_data.get("parent")
        phone_number = students_form.cleaned_data.get("phone_number")

    context= {'students_form':students_form,
               'name': name,
               'gender': gender,
               'school': school,
               'parent': parent,
               'phone_number': phone_number,
               'submit_students_btn': submit_students_btn
               }

    return render(request, 'student.html', context)