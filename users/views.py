from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .users_config import (
    LOGIN_SUCCESS_REDIRECT, LOGIN_FAILURE_REDIRECT, LOGOUT_REDIRECT_URL
)

# GAF_ViewName has been used because names such as LoginView, LogoutView etc.abs
# are too common and may cause clashes if these names are used in a dependency.

class GAF_LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()

        return render(request=request, template_name="users/login.html",
                context = {
                    "login_form": login_form,
                })

    def post(self, request):
        login_form = AuthenticationForm(request, data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged In!")
                return redirect(LOGIN_SUCCESS_REDIRECT)

            messages.error(request, "Authentication unsuccessful. Invalid Username or Password.")
            return redirect(LOGIN_FAILURE_REDIRECT)

class GAF_LogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect(LOGOUT_REDIRECT_URL)

    def post(self, request):
        logout(request)
        return redirect(LOGOUT_REDIRECT_URL)

class GAF_CreateUserView(View):
    def get(self, request):
        user_creation_form = UserCreationForm()

        return render(request=request, template_name="users/register.html",
                context={
                    "user_creation_form": user_creation_form,
                })

    def post(self, request):
        user_creation_form = UserCreationForm(request.POST)

        if user_creation_form.is_valid():
            user = user_creation_form.save()
            # DEBATABLE: Since we have just created this user, we are sure about it's
            # credibility. Therefore, we login without calling authenticate.
            # TO-DO (POSSIBLE): add authenticate call before login
            login(request, user)
            messages.success(request, "Welcome to Generate a Form!")
            return redirect(LOGIN_SUCCESS_REDIRECT)

        messages.error(request, "Invalid details. Couldn't create user.")
        return redirect(LOGIN_FAILURE_REDIRECT)
