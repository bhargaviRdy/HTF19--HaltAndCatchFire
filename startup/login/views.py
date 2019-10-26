from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from register.models import Users
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt

    
# Create your views here.
@csrf_exempt
def login(request):

    all_users=list(Users.objects.values('email'))
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        try :
       
            pw=Users.objects.get(email=email)
            if pw.password==password:
                return redirect('/home/')
            else:
                return render(request,'login2.html',{'message':"Invalid pwd"})
        except:
            return render(request,'login2.html',{'message':"Invalid email"})

    return render(request,"login2.html",{'message':""}) 
    
       
