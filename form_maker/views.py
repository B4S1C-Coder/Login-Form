from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def  index(request):
    if  request.method == 'POST':
        data=request.POST
        Name=data.get('name')
        Rollno=data.get('rollno')
        Branch=data.get( 'branch')
        image=request.FILES.get('image')
        print(Name)
        print(Rollno)
        print(Branch)
    return render(request,"index.html")