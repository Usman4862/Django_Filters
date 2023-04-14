from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= [
        'first_name',
        'last_name',
        'd_o_b',
        'student_class',
        'created_at',
        'updated_at',
    ]