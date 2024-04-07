from django.urls import path
from . import views

app_name = "form_maker"

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("edit-form/<int:id>", views.EditFormView.as_view(), name="editform"),
]