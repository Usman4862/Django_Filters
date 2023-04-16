from django.urls import path
from .views import student_exam

urlpatterns = [
    path('exams/', student_exam, name='student-exam'),
]
