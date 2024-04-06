from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class ApplicationForm(models.Model):    
    form_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    form_name = models.CharField("form_name", max_length=50)
    form_bkg_img = models.ImageField(upload_to="form_bg_images/",
                        blank=True, null=True)
    form_logo_img = models.ImageField(upload_to="form_logo_images/",
                        null=True, blank=True)
    form_specific_questions = models.JSONField('specific_questions')

class FormApplicant(models.Model):
    BRANCH_CHOICES = [
        ('COE', 'Computer Engineering'),
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EEC', 'Electrical and Computer Engineering'),
        ('ENC', 'Electronics and Computer Engineering'),
        ('ME', 'Mechanical Engineering')
    ]

    associated_form = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE)
    applicant_name = models.CharField("applicant_name", max_length=50)
    applicant_rollno = models.IntegerField("applicant_rollno",
                        validators=[MinValueValidator(1)])
    applicant_branch = models.CharField("applicant_branch", max_length=50,
                        choices=BRANCH_CHOICES, default="EEC")
    applicant_email = models.EmailField("applicant_email")
    applicant_photo = models.ImageField(upload_to="applicant_photos/",
                        blank=True, null=True)

