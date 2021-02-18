from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from travello.models import shoes,watches,cloth,perfumes
from travello.filters import Cloth_Shoe_Filter,Watch_Perf_Filter
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# Create your views here.
def f_shoes(request):
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
          shoe = shoes.objects.all()
          myfilter = Cloth_Shoe_Filter(request.GET,shoe)
          shoe = myfilter.qs
          return render(request,'2.html',{'shoes':shoe,'filter':myfilter})
    
    else:
          shoe = shoes.objects.all()
          myfilter = Cloth_Shoe_Filter(request.GET,shoe)
          shoe = myfilter.qs
          return render(request,'2.html',{'shoes':shoe,'filter':myfilter})
    
def m_shoes(request):
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
          shoe = shoes.objects.all()
          myfilter = Cloth_Shoe_Filter(request.GET,shoe)
          shoe = myfilter.qs
          return render(request,'1.html',{'shoes':shoe,'filter':myfilter})
    
        else:
         shoe = shoes.objects.all()
         myfilter = Cloth_Shoe_Filter(request.GET,shoe)
         shoe = myfilter.qs
         return render(request,'1.html',{'shoes':shoe,'filter':myfilter})
    
def f_cloths(request):
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
          cloths = cloth.objects.all()
          myfilter =Cloth_Shoe_Filter(request.GET,cloths)
          cloths = myfilter.qs
          return render(request,'5.html',{'cloths':cloths,'filter':myfilter})

      else:
          cloths = cloth.objects.all()
          myfilter =Cloth_Shoe_Filter(request.GET,cloths)
          cloths = myfilter.qs
          return render(request,'5.html',{'cloths':cloths,'filter':myfilter})

def m_cloths(request):
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
          cloths = cloth.objects.all()
          myfilter =Cloth_Shoe_Filter(request.GET,cloths)
          cloths = myfilter.qs
          return render(request,'4.html',{'cloths':cloths,'filter':myfilter})

        else:
          cloths = cloth.objects.all()
          myfilter =Cloth_Shoe_Filter(request.GET,cloths)
          cloths = myfilter.qs
          return render(request,'4.html',{'cloths':cloths,'filter':myfilter})

def watch(request):

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
          watchs = watches.objects.all()
          myfilter = Watch_Perf_Filter(request.GET,watchs)
          watchs = myfilter.qs
          print('you cart is ',request.session['cart'])
          return render(request,'3.html',{'watchs':watchs,'filter':myfilter})
        else:
         watchs = watches.objects.all()
         myfilter = Watch_Perf_Filter(request.GET,watchs)
         watchs = myfilter.qs
         return render(request,'3.html',{'watchs':watchs,'filter':myfilter})
    
def perfume(request):
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
          perf = perfumes.objects.all()
          myfilter = Watch_Perf_Filter(request.GET,perf)
          perf = myfilter.qs
          print('you cart is ',request.session['cart'])
          return render(request,'6.html',{'perf':perf,'filter':myfilter})
        else:
         perf = perfumes.objects.all()
         myfilter = Watch_Perf_Filter(request.GET,perf)
         perf = myfilter.qs
         return render(request,'6.html',{'perf':perf,'filter':myfilter})


# Create your views here.
