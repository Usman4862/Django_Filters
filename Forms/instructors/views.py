from django.shortcuts import render
from .forms import Instructor
from datetime import date


def instructor(request):
    if request.method == 'POST':
        obj = Instructor(request.POST)
        if obj.is_valid():
            print('Data Validated')
            name = obj.cleaned_data['name']
            email = obj.cleaned_data['email']
            password = obj.cleaned_data['password']
            date_of_birth = obj.cleaned_data['date_of_birth']
            age = (date.today() - date_of_birth).days // 365
            print('Name', name)
            print('Password', password)
            print('Email', email)
            print('Date of Birth', date_of_birth)
            print('Age', age)
        else:
            print('Data not Validated')

    else:
        obj = Instructor
    context = {
        'instructor' : obj,
        'age' : age
    }
    return render(request, 'instructors.html', context=context)


