from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def output(request):
    if request.method=="POST":
        data=request.POST
        Name=data.get('Name')
        print(Name)
        return redirect('/form_output/')
    # querryset=form_maker.Form.objects.all()
    # context={'feilds':querryset}
    context={'feilds':["Name","Age","email","Phone"]}
    return render(request, 'test.html', context)