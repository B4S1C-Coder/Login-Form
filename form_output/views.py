from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def output(request):
    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        age=data.get('age')
        email=data.get('email')
        phone=data.get('phone')
        gender=data.get('gender')
        rno=data.get('rno')
        image=data.get('image')
        print(name)
        print(age)
        print(email)
        print(phone)
        print(gender)
        print(rno)
        print(image)
        return redirect('/form_output/')
        
    # querryset=form_maker.Form.objects.all()
    # context={'feilds':querryset}
    bg_link="https://images.pexels.com/photos/1379636/pexels-photo-1379636.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    footer="/static/assets/images/footer.png"
    header="/static/assets/images/header.png"
    content="this the content that will be displayed"
    feilds=["name","age","email","phone"]
    context={'feilds':feilds,'content':content,"bg_link":bg_link,"footer":footer,"header":header}
    return render(request, 'output.html', context)