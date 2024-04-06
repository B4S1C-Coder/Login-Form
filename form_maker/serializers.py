from rest_framework import serializers
from .models import ApplicationForm

class ApplicationFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = [
            "form_creator",
            "form_bkg_img",
            "form_logo_img",
            "form_specific_questions",
        ]