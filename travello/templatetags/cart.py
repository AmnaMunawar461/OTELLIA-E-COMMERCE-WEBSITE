from travello.models  import * 
from travello.filters import Cloth_Shoe_Filter,Watch_Perf_Filter
from django import template
register = template.Library()
@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    if cart:
     keys = cart.keys()
     for k in keys:
        if product.id == int(k):
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
  if cart: 
    keys = cart.keys()
     
    for k in keys:
        if product.id == int(k):
            return cart.get(k)
    return 0
  else:
   return 0

@register.filter(name='price')
def total_price(product,cart):
   if cart: 
    return   product.price * cart_quantity(product,cart)
   else:
    return 0




@register.filter(name='total_cart')
def total_cart(products,cart):
   if cart:
    sum = 0
    s = 0
    a = 0
    shoe = shoes.objects.all()
    cloths = cloth.objects.all()
    watch = watches.objects.all()
    popul = popular.objects.all()
    c = 0
    o = 0
    w = 0
    for p in products:
        sum += total_price(p,cart)
    for i in shoe:
        s += total_price(i,cart)
    for j in cloths:
        c += total_price(j,cart)
    for p in watch:
        w += total_price(p,cart)
    for e in popul:
        o += total_price(e,cart)
   
        a = sum + s + c + w + o
    return a
   else:
    return 0    
