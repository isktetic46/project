from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


def services(request):
    return render(request,"services.html")


def blogs(request):
    return render(request,"blogs.html")


def login(request):
    
    if request.method=="POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,pass1=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"LOGIN SUCCESSFULL")
            return redirect("/")

    
        else:
            messages.success(request,"invalid credential")
            return redirect("/")
        
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        # print(uname,email,password,confirmpassword)
        if password != confirmpassword:
            
           messages.warning(request,"password does not match")
           return redirect("/signup")
        try:
            if User.objects.get(username = uname):
                messages.info(request,"username already present")
                return redirect("/signup")
        except:
            pass
        
        try:
            if User.objects.get(email= email):
                messages.info(request,"email is taken")
                return redirect("/signup")
        except:
            pass
    
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"signup successfull")
        return redirect("/login")
    
    
    return render(request,'signup.html')