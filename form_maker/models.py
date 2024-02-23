from django.db import models

# Suggestion: Maybe create a config.py file for this app and store BRANCH_CHOICES
# there. This is to increase readability as number of branches increases. Also it
# might be better and possibly more efficient to NOT HAVE BRANCH_CHOICES as an
# attribute of the Form class.
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