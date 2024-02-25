from django.shortcuts import render,HttpResponse

# Create your views here.
def output(request):
    fields = ['name']
    return render(request,'test.html',fields)