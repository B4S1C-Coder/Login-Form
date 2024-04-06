from django.forms import ModelForm
from .models import ApplicationForm

class ApplicationFormForm(ModelForm):
    class Meta:
        model = ApplicationForm
        fields = [
            "form_name",
            "form_bkg_img",
            "form_logo_img",
            "form_specific_questions",
        ]

    def save(self, form_creator, commit=True):
        self.clean()
        app_form = super(ApplicationFormForm, self).save(commit=False)
        app_form.form_creator = form_creator

        if commit:
            app_form.save()
