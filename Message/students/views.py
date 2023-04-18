from django.shortcuts import render
from .forms import StudentForm
from django.contrib import messages


# NOTE: There are two method of messages 
# 1- get_level method 
# 2- set_level method
"""
LEVEL ----- TAG ------ VALUE

Debug ----- debug ----- 10
Info ------ info ------- 20
Success ----- success ----- 25
Warning ------ warning ------ 30
Error --------- error ------ 40
"""

def student_form(request):
    if request.method == 'POST':
        obj = StudentForm(request.POST)
        if obj.is_valid():
            print('Data Validated')
            name = obj.cleaned_data['name']
            email = obj.cleaned_data['email']
            password = obj.cleaned_data['password']
            print('Name', name)
            print('Email', email)
            print('Password', password)
            obj.save()
            # messages.add_message(
            #     request,
            #     messages.SUCCESS,
            #     'Student has been created!!!!!!'
            #     )
            messages.success(
                request,
                'Student has been created!!!!'
            )
            # checking level method of this message
            print('Success Value:', messages.get_level(request))
            messages.info(
                request,
                'Now you can login!!!!'
            )
            # In Debug, first we need to set the level for it
            messages.set_level(request, messages.DEBUG)
            messages.debug(
                request,
                'This is my Debug!!!!!!!!!!!!!'
            )
            # checking level method of this message
            print('Debug Value', messages.get_level(request))

            # Warning
            messages.warning(
                request,
                'This is Warning Tag!!!!!!!!!!'
            )
            print(messages.get_level(request))
            # Error
            messages.error(
                request,
                'This is Error!!!!!!!!!!!!!!!!!!!'
            )
            print(messages.get_level(request))
        else:
            print('Data Not Validated')
    else:
        obj = StudentForm()
    
    context = {
        'form': obj
    }
    return render(request, 'index.html', context=context)