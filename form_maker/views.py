from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ApplicationForm
from .forms import ApplicationFormForm
from .form_maker_config import (
    DASHBOARD_SUCCESS_REDIRECT, DASHBOARD_FAILURE_REDIRECT
)

class DashboardView(View, LoginRequiredMixin):
    def get(self, request):
        create_form = ApplicationFormForm()

        user_forms = ApplicationForm.objects.filter(form_creator__id=request.user.id)

        if len(user_forms) == 0:
            user_forms = ["You don't have any forms yet."]

        return render(request=request, template_name="form_maker/dashboard.html",
                context={
                    "create_form": create_form,
                    "user_forms": user_forms,
                })

    def post(self, request):
        # data = request.POST
        # data["form_creator"] = request.user
        create_form = ApplicationFormForm(request.POST)


        if create_form.is_valid():
            # preprocess specific questions json if needed
            application_form = create_form.save(form_creator=request.user)
            messages.success(request, "Form created successfully.")
            return redirect(DASHBOARD_SUCCESS_REDIRECT)

        user_forms = ApplicationForm.objects.filter(form_creator__id=request.user.id)

        if len(user_forms) == 0:
            user_forms = ["You don't have any forms yet."]

        messages.error(request, f"Couldn't create form.\n{create_form.errors.items}")
        # return redirect(DASHBOARD_FAILURE_REDIRECT)
        return render(request=request, template_name="form_maker/dashboard.html",
                context={
                    "create_form": create_form,
                    "user_forms": user_forms,
                })

