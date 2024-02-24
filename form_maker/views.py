from django.shortcuts import render, redirect
from django.http import HttpResponse

# Django REST imports
from rest_framework import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from knox.auth import TokenAuthentication

from .serializers import HTMLContentSerializer
from .models import *

class FormMakerDashboardView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        data = HTMLContentSerializer(data={
            "content": f"<h1>Logged In: {self.request.user.username}</h1>"
        })
        if data.is_valid():
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
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
