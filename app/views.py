from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Chandu(request):
    return HttpResponse('<marquee><h1>Chandu and shilpa are bestfriends</h1></marquee>')


def Srivalli(request):
    return HttpResponse('<marquee><h1>Endhi ammi nachinana neeku</h1></marquee>')



def Shilpa(request):
    return render(request,'Shilpa.html')


def Amma(request):
    return render(request,'Amma.html')