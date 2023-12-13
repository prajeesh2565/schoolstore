from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.registration,name='register'),
    path('details',views.details,name='details'),
    path('newpage',views.newpage,name='newpage'),
    path('deatils',views.details,name='details')
]
