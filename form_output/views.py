from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def output(request):
    # if request.method=="POST":
    #     data=request.POST
    #     name=data.get('name')
    #     age=data.get('age')
    #     email=data.get('email')
    #     phone=data.get('phone')
    #     gender=data.get('gender')
    #     rno=data.get('rno')
    #     image=data.get('image')
    #     print(name)
    #     print(age)
    #     print(email)
    #     print(phone)
    #     print(gender)
    #     print(rno)
    #     print(image)
    #     return redirect('/form_output/')
        
        
        
    # querryset=form_maker.Form.objects.all()
    # context={'feilds':querryset}
    bg_link="https://images.pexels.com/photos/1379636/pexels-photo-1379636.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    footer="/static/assets/images/footer.png"
    header="/static/assets/images/header.png"
    content="this the content that will be displayed"
    actionUrl="https://docs.google.com/forms/u/0/d/e/1FAIpQLSezmeDQOdNZppr32soj43C1-5jJfxfTkPfemwJyhH2Kq78pJw/formResponse"
    feilds=["name","age","email","phone"]
    feildEntries=["entry.131679070","entry.581217161","entry.1316288904","entry.962543769"]
    context={'feilds':feilds,'content':content,"bg_link":bg_link,"footer":footer,"header":header,"actionUrl":actionUrl}
    return render(request, 'output.html', context)


# entry.131679070=name&
# entry.581217161=age&
# entry.1316288904=email
# &entry.962543769=phone
# &entry.1290990780=Male
# &entry.504840661=rollno
# https://docs.google.com/forms/d/e/1FAIpQLSezmeDQOdNZppr32soj43C1-5jJfxfTkPfemwJyhH2Kq78pJw/formResponse
