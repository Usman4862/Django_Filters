from django.contrib import admin
from django.urls import path
from enroll.views import register, user_login, profile, user_logout, change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('change-password/', change_password, name='change-password'),
]
