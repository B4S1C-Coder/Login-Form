# This is a prototype for a REST API for the form_maker app
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from form_maker.models import Form
from .serializers import FormSerializer

class FormView(APIView):

    def post(self, request, format=None):
        """ Submit the filled form. Data is should be in JSON format. """
        form_data = FormSerializer(data=self.request.data)

        if form_data.is_valid():
            form_data.save()
            return Response({
                "detail": "Form submitted successfully"
            }, status=status.HTTP_201_CREATED)
        
        return Response(form_data.errors, status=status.HTTP_400_BAD_REQUEST)
