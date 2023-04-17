from django.urls import path
from .views import instructor

urlpatterns = [
    path('instuctor/', instructor, name='instructor'),
]
