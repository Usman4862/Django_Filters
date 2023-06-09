from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('enroll.urls')),
    path('student/', include('exams.urls')),
    path('', include('instructors.urls')),
]
