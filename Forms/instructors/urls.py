from django.urls import path
from .views import instructor

urlpatterns = [
    path('instructor/', instructor, name='instructor'),
]
