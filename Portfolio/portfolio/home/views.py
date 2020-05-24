from django.shortcuts import render
from django.http import HttpResponse
from.models import Contact,Projects
# Create your views here.
def index(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        desc = request.POST['desc']
        contact = Contact(name=name,desc=desc)
        contact.save()
    return render(request,'home/contact.html')

def projects(request):
    prod = Projects.objects.all()
    context = {'prod':prod}
    return render(request,'home/project.html',context)            