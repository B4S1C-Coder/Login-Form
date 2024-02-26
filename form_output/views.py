from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def output(request):
    if request.method=="POST":
        # data=request.POST
        # content=data.get('Name')
        # print(content)
        return redirect('/form_output/')
        
    # querryset=form_maker.Form.objects.all()
    # context={'feilds':querryset}
    bg_link="https://images.pexels.com/photos/1379636/pexels-photo-1379636.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    footer=""
    header=""
    context={'feilds':["Name","Age","Email","Phone"],'content':"this the content that will be displayed","bg_link":bg_link,"footer":footer,"header":header}
    return render(request, 'output.html', context)