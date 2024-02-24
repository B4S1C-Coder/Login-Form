from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def  index(request):
    if  request.method == 'POST':
        data=request.POST

        name = data.get('name')
        email = data.get('email')
        age = data.get('age')
        phone = data.get('phone')
        gender = data.get('gender')

        # Name=data.get('name')
        # Rollno=data.get('rollno')
        # Branch=data.get( 'branch')
        # image=request.FILES.get('image')
        # print(Name)
        # print(Rollno)
        # print(Branch)
        # print(image)
        # return redirect('/')
    return render(request,"index.html")