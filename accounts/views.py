from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from travello.models import perfumes,shoes,cloth,watches,popular
# Create your views here.
def finish(request):
    if request.method == 'POST':
        address = request.POST['address']
        number = request.POST['number']
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        request.session['cart']={}
        print(request.session['cart'])
        return redirect('cart')

def checkout(request):
    return render(request,'checkout.html')
def cart(request):
    if request.method == 'GET':
       cart = request.session['cart']
       if cart: 
        ids = list(request.session.get('cart').keys())
        product = perfumes.get_product_by_id(ids)
        shoe = shoes.get_product(ids)
        w = watches.get_watch(ids)
        c = cloth.get_cloths(ids)
        p = popular.get_popular(ids)
        print(product,w,c,p)
        return render(request,'cart.html',{'products':product,"shoes":shoe,"watch":w,"cloth":c,"popular":p})
       else:
           return render(request,'card1.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            request.session['customer_id']=user.id
            request.session['email'] = user.email
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
         return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is in use!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists!')
                return redirect('register')
            else:
              user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
              user.save()
              print('user created')
              return redirect('login')
        else:
             messages.info(request,'password not matching!')
             return redirect('register')
        
    else:
        return render(request,'register.html')
