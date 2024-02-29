from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Django REST imports
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from knox.auth import TokenAuthentication

from .serializers import FormMetaDataSerializer
from .models import FormMetaData

class FormMakerInterfaceView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request=request, template_name="form_maker/dashboard.html")

# MEANT TO BE USED BY THE FRONTEND ONLY
class InterfaceFormCreationDataAPIView(APIView):

    def post(self, request):
        # check if user is logged in
        if not request.user.is_authenticated():
            return Response({'detail':'User is not authenticated.'},
                status=status.HTTP_401_UNAUTHORIZED)

        form_meta_data_serializer = FormMetaDataSerializer(data=self.request.data)

        if form_meta_data_serializer.is_valid():
            form_meta_data_serializer.save()
            return Response({
                "detail": "Form data saved.",
                "redirect_url": "some url for form_output"},
                status=status.HTTP_201_CREATED)
        else:
            return Response(form_meta_data_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     bg_img = request.FILES.get("bg_img")
        #     logo_img = request.FILES.get("logo_img")
        # except Exception as err:
        #     return Response({'detail': f'Bad data.\nError: {err}'},
        #         status=status.HTTP_400_BAD_REQUEST)

        # form_meta_data_serializer = FormMetaDataSerializer(data={
        #     'user': request.user,
        #     'background_image': bg_img,
        #     'logo_image': logo_image,
        #     'specific_questions_json': request.data['specific_ques']
        # })


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
