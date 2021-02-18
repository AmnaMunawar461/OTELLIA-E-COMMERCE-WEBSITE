from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
# Create your views here.
def destinations(request):
    if request.user.is_authenticated:
        return render(request,'destination.html')
    else:
        messages.info(request,'Login /Register First ')
        return redirect('/')
