from django.shortcuts import render
from django.http import HttpResponse
from HM_FoundationApp.models import Executive_Counsil,Adviser_Counsil,Add_News,Add_Image
# Create your views here.
def index(request):
    anData = Add_News.objects.all()
    imageData = Add_Image.objects.all()
    data={
        'anData':anData,
        'imageData':imageData
    }
    return render(request,'index.html',data)
    
    
def allmember(request):
    ecData = Executive_Counsil.objects.all()
    acData = Adviser_Counsil.objects.all()
    data={
        'ecData':ecData,
        'acData':acData
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
def donation(request):
    return render(request,'donation.html')
def secretary(request):
    return render(request,'secretary.html')