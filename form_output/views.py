
from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
# Create your views here.
def output(request):
    
    bg_link="https://images.pexels.com/photos/1379636/pexels-photo-1379636.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    footer="/static/assets/images/footer.png"
    header="/static/assets/images/header.png"
    formtitle="form title"
    content="this the content that will be displayed"
    fields=["Name","Age","Email","Phone","Rollno"]
    
    if request.method=='post':
        return redirect('/form_output')
        
        
    # querryset=form_maker.Form.objects.all()
    # context={'feilds':querryset}
    context={
        'fields':fields,
        'content':content,
        "bg_link":bg_link,
        "footer":footer,
        "header":header,
        "formtitle":formtitle,
    }
   
    
    return render(request,'test.html',context)


def submit(request):
    actionUrl="https://docs.google.com/forms/u/0/d/e/1FAIpQLSezmeDQOdNZppr32soj43C1-5jJfxfTkPfemwJyhH2Kq78pJw/formResponse"
    fields=["Name","Age","Email","Phone","Rollno"]
    Entries=["entry.131679070","entry.581217161","entry.1316288904","entry.962543769","entry.504840661"]
    fieldData=list(zip(fields,Entries))
    
    # entry.131679070=name&
    # entry.581217161=age&
    # entry.1316288904=email&
    # entry.962543769=phone&
    # entry.1290990780=Male&
    # entry.504840661=rollno&
    # https://docs.google.com/forms/d/e/1FAIpQLSezmeDQOdNZppr32soj43C1-5jJfxfTkPfemwJyhH2Kq78pJw/formResponse

    
    
    if request.method == 'POST':
    # do something with the request data
        data=request.POST
        name=data.get('Name')
        age=data.get('Age')
        email=data.get('Email')
        phone=data.get('Phone')
        rollno=data.get('Rollno')
        gender=data.get('gender')
        print(name)
        print(age)
        print(email)
        print(phone)
        print(rollno)
        print(gender)
        # return JsonResponse({"success": True})
        return redirect('/admin') 
    return HttpResponse("JSON data not reached. Please ensure that a POST request was made with valid JSON data.")