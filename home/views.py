from django.shortcuts import render
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    return request, 'login.html'
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        name = request.POST.get('name')
        contact = Contact(name= name, email = email, message = message, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent")
        return render(request, 'contact.html')
    