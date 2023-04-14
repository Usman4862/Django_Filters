from django.shortcuts import render
from .models import Student
from datetime import *



def student_list(request):
    students = Student.objects.all()
    paragraph = '''this is ihjiojkjsalkfj fkljdsdklj lksdnflkds nfljksdnflksd nlknflk descriptionsdflkndslkfnd
            sdlfnlksdn klsdn klfndklfn kldnfkl dsnf lkdsnklnlksd nlknflksdlkadsm fkldslkdfnm kldsfmlds
            salflk sdmf klsdkldsfdkl  sdlkfj kldsd jfkldsjf lksdjf jfkldsjflslkdjf flksdmklsd lksdjf
            this is the first time ever we need to do with your own responsibility for the last time to use it.
            this is the random swamped paragraph, now i think you should need to change your mind.'''
    slicing_test = 'this is a slicing test, so don"t be worry about it, understood.' 
    context = {
        'students': students,
        'p' : paragraph,
        'mother_number' : False,
        's': slicing_test
    }
    return render(request, 'index.html', context=context)
