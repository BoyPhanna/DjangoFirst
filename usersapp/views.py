from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        if username=="" or email=="" or password=="":
            messages.warning(request,"សូមបញ្ចូលទិន្នន័យឲ្យគ្រប់")
            return redirect("/register")
        else:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"ឈ្មោះនេះមានអ្នកប្រើហើយសូមបញ្ចូលឈ្មោះថ្មី")
                return redirect("/register")
            else:
                messages.success(request,"បង្កើតគណនីជោគជ័យ")
                user=User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                return redirect("/register")
    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if username==""  or password=="":
            messages.warning(request,"សូមបញ្ចូលទិន្នន័យឲ្យគ្រប់")
            return redirect("/login")
            
        else:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.warning(request,"ឈ្មោះឬលេខសម្ងាត់ខុស")
                return redirect("/login")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/login")
