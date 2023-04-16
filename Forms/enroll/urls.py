from django.urls import path
from . import views

urlpatterns = [
    path('enroll/', views.student_registration_view, name='student-registration'),
    path('info/', views.student_info, name='student-info'),
]
