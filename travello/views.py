from django.shortcuts import render
from .models import popular

# Create your views here.
# Create your views here.

def index(request):
    if request.method == 'POST':
          product=request.POST['id']
          remove=request.POST['remove']
          cart = request.session.get('cart')
          if cart:
              quantity=cart.get(product)
              if quantity:
                  if remove == 'True':
                      if quantity<=1:
                          cart.pop(product)
                      else:
                          cart[product]=quantity -1;
                  elif remove =='False':
                      cart[product]=quantity +1;
              else:
                cart[product]=1;    
          else:
              cart={}
              cart[product]=1;
          request.session['cart']=cart
          print('you cart is ',request.session['cart'])
          
          p = popular.objects.all()
          print('your email is',request.session.get('email'))
          return render(request,'index.html',{'popular':p})
    
    else:
          p = popular.objects.all()
          print('your email is',request.session.get('email'))
          return render(request,'index.html',{'popular':p})
    
