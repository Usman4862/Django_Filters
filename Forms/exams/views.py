from django.shortcuts import render
from .forms import StudentExam


def student_exam(request):
    if request.method == 'POST':
        fm = StudentExam(request.POST)
        if fm.is_valid():
            print('Data Validated')
            name = fm.cleaned_data['name']
            bio = fm.cleaned_data['bio']
            password = fm.cleaned_data['test']
            email = fm.cleaned_data['email']
            print('Name', name)
            print('Bio', bio)
            print('Test', password)
            print('Email', email)
    else:
        fm = StudentExam()
    context = {
        'exam_form' : fm
    }
    return render(request, 'exam.html', context=context)