from django.urls import path
from .views import DashboardView

app_name = "form_maker"

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]