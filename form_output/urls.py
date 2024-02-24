from django.urls import path
from . import views

urlpatterns = [
    path('/form_output', views.output, name="output"),
] 