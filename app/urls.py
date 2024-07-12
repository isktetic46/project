from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about.html'),
    path('contact',views.contact,name='contact.html'),
    path('services',views.services,name='services.html'),
    path('blogs',views.blogs,name='blogs.html'),
    path('login',views.login,name='login.html'),
    path('signup',views.signup,name='signup.html'),
    
]
