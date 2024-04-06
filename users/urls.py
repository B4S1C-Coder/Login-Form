from django.urls import path
from .views import GAF_LoginView, GAF_CreateUserView, GAF_LogoutView

app_name = "users"

urlpatterns = [
    path("login/", GAF_LoginView.as_view(), name="login"),
    path("logout/", GAF_LogoutView.as_view(), name="logout"),
    path("create-user/", GAF_CreateUserView.as_view(), name="createuser"),
]