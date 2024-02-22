from django.db import models

# Create your models here.

class Form(models.Model):
    BRANCH_CHOICES = [('COE','Computer Engineering'),
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
    ]
    name=models.CharField(max_length=100)
    rollno=models.IntegerField(default=0)
    branch=models.CharField(max_length=50,choices=BRANCH_CHOICES,default="CSE")
    image=models.ImageField(upload_to='images/',blank=True)