from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# importing message in views
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        "variable1":"Susheel is larning",
        "variable2":"and working"
    }
    messages.success(request,'this is a test message')
    return render(request,"index.html",context)
    # return render(request,"index.html")

def about(request):
    # return HttpResponse("this is about page")  
    return render(request,"about.html")

def services(request):
    # return HttpResponse("this is services page")
    return render(request,"services.html")  

def contact(request):
    # return HttpResponse("this is contact page")  
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been send.')
    return render(request,"contact.html") 
