from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import *

def S_Form(request):
    SFO=Student()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=Student(request.POST)

        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        
        else:
            return HttpResponse('Data is not Valid')
    return render(request, 'S_Form.html', d)


def T_Form(request):
    TFO=Topic_Form()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=Topic_Form(request.POST)

        if TFD.is_valid():
            TFD.save()
            return HttpResponse(str(TFD.cleaned_data))
        
        else:
            return HttpResponse('Data is not Valid')
    return render(request, 'T_Form.html', d)
