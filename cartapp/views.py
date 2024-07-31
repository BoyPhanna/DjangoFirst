from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from productapp.models import Product
from cartapp.models import Cart,CartItem


def create_cartid(request):
    # ទាញយកអត្ដលេខ ម្ចា់គណនី
    cart=request.session.session_key
    if not cart:
        # ប្រសិនបើគ្មាន ឲ្យបង្កើត
        cart=request.session.create()
    return cart


@login_required(login_url="/login")
def removeCart(request,product_id):
    print(product_id)
    cart=Cart.objects.get(cart_id=create_cartid(request),customer=request.user)
    product=Product.objects.get(pk=product_id)
    cartItem=CartItem.objects.get(product=product,cart=cart)
    cartItem.delete()
    return redirect("/cart")

# Create your views here.
@login_required(login_url="/login")
def cart(request):
    counter=0
    total=0
    try:
        # ទាញយកនូវកាត្រកដែលត្រូវនឹង cart_id ដែលអ្នកប្រើចុច
        cart=Cart.objects.get(cart_id=create_cartid(request),customer=request.user)

        # ទាញទិន្នន័យផលិតផលពីកាត្រក
        cartItem=CartItem.objects.filter(cart=cart)
        for item in cartItem:
            counter+=item.quantity
            total+=item.product.price*item.quantity
    except (Cart.DoesNotExist,CartItem.DoesNotExist):
        # ប្រសិនបើគ្មានការបង្កើតការត្រកទេ
        cart=None
        cartItem=None
    return render(request,"cart.html",{"cartItem":cartItem,"total":total,"counter":counter})



@login_required(login_url="/login")
def addCard(request,product_id):
    product=Product.objects.get(pk=product_id)
    # បង្កើតការត្រក
    try:
        # មានកាត្រក
        cart=Cart.objects.get(cart_id=create_cartid(request))
    except Cart.DoesNotExist:
        # មិនទាន់មានការត្រក បង្កើតការត្រករួចរករក្សាតទុកក្មុងមូលទិនន័យ
        cart=Cart.objects.create(
            cart_id=create_cartid(request),
            customer=request.user
        )
        cart.save()
    # កត់ត្រារាយនាមផលិតផល
    try:
        cartItem=CartItem.objects.get(product=product,cart=cart)
        if cartItem.quantity < cartItem.product.stock:
            cartItem.quantity+=1
            cartItem.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
    return redirect("/cart")