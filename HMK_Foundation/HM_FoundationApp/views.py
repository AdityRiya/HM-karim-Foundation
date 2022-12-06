from django.shortcuts import render
from django.http import HttpResponse
from HM_FoundationApp.models import Executive_Counsil
# Create your views here.
def index(request):
    return render(request,'index.html')
def allmember(request):
    ecData = Executive_Counsil.objects.all()
    data={
        'ecData':ecData
    }
    return render(request,'AllMember.html',data)
def chairman(request):
    return render(request,'chairman.html')
def contact(request):
    return render(request,'contact.html')
def mission(request):
    return render(request,'mission.html')
def services(request):
    return render(request,'services.html')
def vision(request):
    return render(request,'vision.html')
def secretary(request):
    return render(request,'secretary.html')