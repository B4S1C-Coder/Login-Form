from django.urls import path
from . import views

urlpatterns = [
    path('',views.output, name="output"),
    path('submit',views.submit, name="submit"),
    
] 