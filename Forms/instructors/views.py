from django.shortcuts import render
from .forms import Instructor


def instructor(request):
    if request.method == 'POST':
        obj = Instructor(request.POST)
        if obj.is_valid():
            print('Data Validated')
            name = obj.cleaned_data['name']
            email = obj.cleaned_data['email']
            password = obj.cleaned_data['password']
            print('Name', name)
            print('Password', password)
            print('Email', email)
        else:
            print('Data not Validated')

    else:
        obj = Instructor
    context = {
        'instructor' : obj
    }
    return render(request, 'instructors.html', context=context)


