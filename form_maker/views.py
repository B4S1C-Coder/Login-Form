from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
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
                    "username": request.user.username,
                })

    def post(self, request):
        create_form = ApplicationFormForm(request.POST, request.FILES)

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
                    "username": request.user.username,
                })

class EditFormView(View, LoginRequiredMixin):
    def get(self, request, id):
        application_form = ApplicationForm.objects.filter(id=id).first()

        if application_form:

            if application_form.form_creator != request.user:
                return HttpResponse("Access denied.")

            create_form = ApplicationFormForm(instance=application_form)
            return render(request=request, template_name="form_maker/editform.html",
                    context={
                        "create_form": create_form,
                        "formname": application_form.form_name,
                    })

        else:
            messages.error(request, "Requested form was not found.")
            return redirect(DASHBOARD_FAILURE_REDIRECT)

    def post(self, request, id):
        application_form = ApplicationForm.objects.filter(id=id).first()

        if application_form:

            if application_form.form_creator != request.user:
                return HttpResponse("Access denied.")

            create_form = ApplicationFormForm(request.POST, request.FILES, instance=application_form)

            if create_form.is_valid():
                create_form.save(form_creator=request.user)
                messages.success(request, f"Form '{application_form.form_name}' updated successfully. ")
                return redirect(DASHBOARD_SUCCESS_REDIRECT)

        else:
            messages.error(request, "Requested form was not found.")
            return redirect(DASHBOARD_FAILURE_REDIRECT)