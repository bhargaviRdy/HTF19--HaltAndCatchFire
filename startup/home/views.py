from django.shortcuts import render
from django.http import HttpResponse
from .models import StartupList
from django.views.decorators.csrf import csrf_exempt

    
# Create your views here.

# from  .models  
def index(request):
    return render(request,'frontpage.html')
def home_view(request):
    all_list=StartupList.objects.all()
    return render(request,'home.html',{'startups':all_list})
@csrf_exempt
def filter(request):
    all_list=StartupList.objects.all()
    apcit=request.POST.getlist('cities[]')
    techs=request.POST.getlist('tech[]')
    print(apcit,techs)
    if(apcit!=[] and techs==[]):
        x=StartupList.objects.filter(location__in=apcit)
    elif apcit==[] and techs!=[]:
        x=StartupList.objects.filter(technology__in=techs)
    else:
        x=StartupList.objects.filter(location__in=apcit).filter(technology__in=techs)
        print(x)
    return render(request,'home.html',{'startups':x})
# Create your views here.
