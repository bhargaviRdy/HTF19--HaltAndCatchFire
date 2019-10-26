from django.shortcuts import render,redirect
from .models import Users
# from django.shortcuts import render
# Create your views here.
# def register(request):
#     return render(request,'register.html')
def register(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        user=Users(name=name,email=email,password=password)
        user.save()
        return redirect('/home/')

    return render(request,'register.html')