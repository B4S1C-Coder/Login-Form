from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.FormMakerInterfaceView.as_view(), name="dashboard"),
    path('submitformdata/', views.InterfaceFormCreationDataAPIView.as_view(), name="submitformdata")
]