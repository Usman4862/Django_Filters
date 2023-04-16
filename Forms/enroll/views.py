from django.shortcuts import render
from .forms import StudentsRegistration

def student_registration_view(request):
    #NOTE:
    # label_suffix is used to edit the input title name
    # initial is used to give a default value to each field
    form_object = StudentsRegistration(
        label_suffix=' ',
        initial={
        'name': 'Usman Malik',
        'email': 'usman@gmail.com',
        'age': 23
        }
    )
    # order fields is used to ordering the form fields, it doesn't matter what is the order of that fields in forms.py or models.py
    form_object.order_fields(
        field_order=[
        'email',
        'name',
        'age',
        ]
    )
    context = {
        'form': form_object
    }
    return render(request, 'index.html', context=context)


def student_info(request):
    form_obj = StudentsRegistration()
    context = {
        'info_form': form_obj
    }
    return render(request, 'student_info.html', context=context)