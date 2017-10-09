from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    # return HttpResponse("manikandan")
    return render(request,'index.html',locals())