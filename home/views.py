from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Images, Clients, Franchise, Employee, Products, Machines, Credentials
# Create your views here.

def home(request):
    images = Images.objects.all()
    clients = Clients.objects.all()
    franchise = Franchise.objects.all()
    return render(request, 'home/index.html',{'images':images,'clients':clients,'franchise':franchise})

def about(request): 
    images = Images.objects.all()
    employee = Employee.objects.all()
    return render(request, 'home/about.html',{'employee':employee,'images':images})

def products(request):
    images = Images.objects.all()
    products = Products.objects.all()
    machines = Machines.objects.all()
    credentials = Credentials.objects.all()
    return render(request, 'home/products.html',{'products':products,'machines':machines,'credentials':credentials,'images':images})

def contact(request):
    if request.method == "POST":
        #print(request)
        name = request.POST.get("name",'default')
        email = request.POST.get("email",'')
        phone = request.POST.get("phone",'')
        msg = request.POST.get("msg",'')
        #print(name, email, phone, desc)
        #saving contact in databse
        contact = Contact(name =name, email = email, phone = phone, msg = msg)
        contact.save() #IMP LINE
    return render(request, 'home/contact.html')


