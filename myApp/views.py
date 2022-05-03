from datetime import datetime
from django.shortcuts import render
from myApp.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contacts = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contacts.save()
        messages.success(request, 'Your message was sent bro')
    return render(request, 'contact.html')
