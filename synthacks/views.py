# Create your views here.
from django.shortcuts import render
from .forms import Form
from .models import *
def index(request):

    return render(request, 'home.html')
def contact(request):

    return render(request, 'contact.html')

def registration(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            name = form.save()
            return render(request, 'index.html')
    else:
        form = Form()

    context={'form':form}

    return render(request, 'registration.html',context)
