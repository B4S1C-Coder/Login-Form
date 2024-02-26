from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def output(request):
    if request.method=="POST":
        data=request.POST
        content=data.get('Name')
        print(content)
        return redirect('/form_output/')
    # querryset=form_maker.Form.objects.all()
    # context={'feilds':querryset}
    context={'feilds':["Name","Age","Email","Phone"],'content':"this the content that will be displayed"}
    return render(request, 'test.html', context)